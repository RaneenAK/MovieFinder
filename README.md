# MovieFinder
Final Project including mongoDB, Docker , Flask and python

Dockerized Flask-Mongo App Project
פרטים לינקים והנחיות
מטרות התרגיל:
Web api
Docker
Docker compose
Mongodb
Flask
עבודה עם גי ט
אבטחה )עבודה עם מפתח API)
תאור הפרויקט:
בפרויקט זה עליכם לפתח שירות המאפשר גישה תכנותית דרך האינטרנט,
למאגר מידע של תמונות )פוסטרים של סרטים(.
המאגר מבוסס mongoDB , בתוכו ישמרו קבצי הסרטים ומידע על הקבצים )שם
סרט, קוד IMDB וכו'(
התוכנה מבוססת flask.
על התוכנה ובסיס הנתונים להיות "עטופים בקונטיינרים "
על התוכנה לממש את האפשרויות הבאות כ web API:
1 . חיפוש פוסטר במאגר )יחזיר קובץ תמונה, במידה ואין במאגר יועבר
החיפוש ל TMDB)
2 . מחיקת פוסטר מהמאגר .
3 . עדכון פרטים על הפוסטר .
בנוסף התוכנה תאפשר את החיפוש גם בעזרת טופס HTML שיהיה נגיש בעזרת
דפדפן .
1 . תכנון מבנה הפרויקט
a . קבצים, תיקיות וכו'
b . שימו לב ל modules and packages
c . שימו לב לעבודה על פרויקט בסביבה ווירטואלית ) venv)
d . פרמטרים )איזה פורטים, שמות של הוסטי ם, מפתחות וכו'(
2. יצירת תשתית בגיט וגיט האב לשיתוף פעולה של הצוות .
a . קראו על git team workflow תכננו את אופי העבודה בגיט
כצוות
-and-teams-small-for-workflow-https://hackandslash.blog/gitrepository/-single guide/-https://rogerdudler.github.io/git
b . דאגו לסנכרן את פאיצ'ארם עם חש בון הגיטהאב שרלוונטי
לפרויקט .
3 . בניית אפליקציה פשוטה המשתמשת ב API של TMDB להוריד פוסטרים של
תמונות לאחר חיפוש ושמירה בתיקיית קבצים.
-movie-the-with-posters-download-https://bin.re/blog/tutorialpython/-in-api-database עליכם לבנות את האפליקציה בחלוקה לקבצים ובאופן מודולרי.בהמשך
הממשק הולך להשתנות )ממשק המשתמש והשכבה שבה שומרים את
הנתונים( .
a . שימוש ב web api של TMDB )שימו לב להתייחסות למפתח והיכן
שומרים אותו(
keys-api-https://sd18spring.github.io/notes/storing -api-store-securely-to-https://www.freecodecamp.org/news/how4ff3ea19ebda/-keys
b . מציאת קוד IMDB לסרט )מקל על החיפוש ב TMDB) -a-searching-imdbpy-https://www.geeksforgeeks.org/pythonmovie/
4 . תכנוןן ובניית מנגנון שמירה לקבצי סרטים במונגו.
במודול נפרד )קובץ( יש לממש CRUD מלא
a . קריאה של קובץ מה DB
b . כתיבה של קובץ ל DB )רשות - לא בפונקציונאליות הסופית (
c . עדכון ערך ברשומ ה
d . מחיקה של רשומ ה
)יש אתגר של שמירת קבצים בינאריים גדולים ב DB) https://pymongo.readthedocs.io/en/stable/examples/gridfs.html
2g73-python-via-mongodb-in-images-ehttps://dev.to/thenishant/stor
קריאת קבצים ממונגו
python/-using-gridfs-https://psabhay.com/posts/mongodb/mongodb
5 . שילוב של שני המודולים יחד - יצירת מודול המייצג את השילוב של
שניהם - ממשק פשוט כשלב ביניים לפני יצירת ממשק ווב י
6 . שימוש בפלאסק של פייתון )פריימוורק וובי שנותן גם פרונט וגם
בק( ליצירת ממשק ו API עבור חיפוש פוסטר
-api-crud-restful-create-to-https://ishmeet1995.medium.com/howb73c5bc8f6cc-docker-and-mongodb-flask-python-with יש ליצור בעזרת web api פעולות CRUD עבור מונגו
a . קריאה של קובץ מה DB
b . כתיבה של קובץ ל DB ) רשות - לא בפונקציונאליות הסופית(
c . עדכון ערך ברשומ ה
d . מחיקה של רשומ ה
יש ליצור ממשק HTML פשוט לקלט חיפוש סרט ) template render using flask)
7 . לעטוף את מונגו בדוקר )שימוש באימג' מוכן(
)נמצא בלינק בסעיף 6 )
8 . לעטוף את האפליקציה בדוקר
https://zetcode.com/python/docker/ )מידע נוסף נמצא בלינק בסעיף 6 )
9 . לחבר בין כולם ולתת להם לנגן מומלץ לקרוא על docker compose לפני
)נמצא בלינק בסעיף 6 )
10 . יצירת קובץ user data שיתקין דוקר, ייקח את הגרסה האחרונה
מהגיט, ייצור את האימג'ים וירים את הקונטניינרים. )שימו לב
למפתח (
11 . להרים EC2 ב sandbox עם ה user data ולראות שאכן האפליקציה
עולה ועובדת.
עוד לינקים על דוקר :
-machine-and-compose-with-flask-https://realpython.com/dockerizingcloud/-the-to-localhost-from
-elasticsearch-docker-python-sentiment-https://realpython.com/twitterkibana/
docker/-versions-//realpython.com/pythonhttps:
למתקדמים:
• לכתוב סקריפט המתחבר ל AWS בעזרת ה CLI מגדיר תשתית ומרים את ה
EC2 עם user data באופן אוטומטי.
• guide/-ultimate-boto3-ec2-https://www.learnaws.org/2020/12/16/aws
• ליצור AMI מה EC2 עם הדוקרים ולנסות להרים את מעבדת איזון
העומסים עם ה AMI שבנינו
