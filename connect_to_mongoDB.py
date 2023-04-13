import pymongo
import requests
import io
from PIL import Image
from passwords_and_keys import mongo_db_password as mpw


username = "user"
password = mpw

# build the connection URI
#uri = f'mongodb+srv://Team5:5teamaws@cluster0.ndyqms7.mongodb.net/?retryWrites=true&w=majority'
uri = f'mongodb://{username}:{mpw}@localhost:27017/Team5'
#uri = "mongodb://localhost:27017/Team5"

# connect to the database using the URI
client = pymongo.MongoClient(uri)

# access a collection
db = client["Team5"]
collection = db["Team5Posters"]

def create_mongo_user():
    # check if user exists
    users_dict = db.command("usersInfo")
    users_list = users_dict['users']
    #print(users_list)

    if len(users_list) > 0:
        for user_dict in users_list:
            user_list_tup = user_dict.items()
            for user_data in user_list_tup:
                if user_data[0] == username and user_data[1] == username:
                    print(f'User {username} already exists')
    else:
        # create user with read/write permissions to 'posters' collection
        db.command("createUser", "user", pwd=mpw, roles=[{"role": "readWrite", "db": "TMDB_posters"}])
        print(f'User {username} created successfully')


def find_poster_in_mongo(movie_title):
    create_mongo_user()
    movie_title = movie_title.lower()
    query = {"movie_title": movie_title}
    results = collection.find(query)
    results = list(results)
    if len(results) > 0:
        first_result = list(results)[0]
        return first_result



#document = {'movie_title': 'Avatar'}
#collection.insert_one(document)

#find_poster_in_mongo("bla")

# define a function to save the image to MongoDB
def save_poster_to_mongo(movie):
    create_mongo_user()
    # download the image from poster_path
    response = requests.get(f"https://image.tmdb.org/t/p/original/{movie['poster_path']}")
    image_binary = io.BytesIO(response.content).getvalue()
    movie_title = movie["title"]
    # Each poster in mongo will look like this:
    document = {
        "movie_title": movie_title.lower(),
        "TMDB_id": movie["id"],
        "poster": image_binary
    }

    collection.insert_one(document)



"""movie = {'adult': False, 'backdrop_path': '/vL5LR6WdxWPjLPFRLe133jXWsh5.jpg', 'genre_ids': [28, 12, 14, 878],
         'id': 65871, 'original_language': 'en', 'original_title': 'Nataly',
         'overview': 'In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.',
         'popularity': 386.424, 'poster_path': '/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg', 'release_date': '2009-12-15',
         'title': 'The Note Book', 'video': False, 'vote_average': 7.569, 'vote_count': 28849}"""

#save_poster_to_mongo(movie)

def delete_poster_from_mongo(movie_title):
    create_mongo_user()
    collection.delete_one({'movie_title': movie_title})
    return f'Poster {movie_title} was deleted'