DJango Commands
Initialize Project: django-admin startproject django_mongo
Initialize App: python manage.py startapp legendary_animals

Mongo Commands (Shell)
To open mongo shell in cmd: mongosh
Show all DB's: show dbs
Use/Create DB: use legangaryAnimalDB 
Create Collection(Table): 

To import .json file
Open cmd in .json file directory: mongoimport --collection=Animals --db=legendaryAnimalsDB --type=json --jsonArray animal_sightings.json

To read files on cmd prompt on mongoshell
show dbs
use legendaryAnimalsDB > show collections > db.Animals(collection).find(); 

Copy connection string from mongo shell/open

pymongo steps:
create db_connecxion.py > import lib and initialize url(db connection string) > pass to mongoclient > initialize db variable > in models.py import db var and initialize collection > in views.py import collection and create views that return Httpresponse

Modules used 
dhongo
dnspython