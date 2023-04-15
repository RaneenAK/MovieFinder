import base64
from flask import Flask, current_app, render_template, request, url_for, make_response, flash, redirect
from connect_to_TMDB import find_poster
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home")
def homey():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/FindAPoster")
def FindAPoster():
    return render_template('FindAPoster.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/find_movie', methods=['POST'])
def find_movie():
    title = request.form['movie_title']
    movie = find_poster(title)
    if type(movie) == dict: #If we found the movie in mongo we get a dict as a return value
        response = make_response('<h1>Movie {} found in Mongo</h1><img src="data:image/jpeg;base64,{}">'.format(movie['movie_title'], base64.b64encode(movie['poster']).decode()))
    elif "https" in movie[1]:#if we found the movie in TMDB we get a list [movie_title, poster_url]
        movie_title, poster_url = movie
        response = make_response('<h1>Movie {} found in TMDB</h1><img src="{}">'.format(movie_title, poster_url))
    else:#if movie isn't found - just show the error message that we receive from find_poster function (if not movies_list:)
        response = make_response('<h1>{}</h1>'.format(movie))
    response.headers['Content-Type'] = 'text/html'
    return response


if __name__ == '__main__':
    app.run(debug=True)
