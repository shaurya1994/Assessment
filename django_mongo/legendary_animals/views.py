from django.shortcuts import render

from .models import animal_collection
from django.http import HttpResponse
from pymongo import MongoClient

# Connection details
connection_string = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6"
client = MongoClient(connection_string)


# Connect to the database and collection
db = client['legendaryAnimals']
animal_collection = db['Animals']
 

# Create your views here.
def index(request):
    return HttpResponse("<h1> Legendary Animals </h1>")

def add_animal(request):
    records = {
        'animal_name' : 'test_animal',
        'state_name' : 'test_state'
    }
    animal_collection.insert_one(records) 

def get_all_animals(request):
    legend = animal_collection.find() # use this to query the db
    return HttpResponse(legend)

def get_one_animal(request):
    animals = animal_collection.find({'animal_name': 'White Tiger'}) # use this to query the db
    return HttpResponse(animals)