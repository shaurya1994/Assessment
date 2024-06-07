from django.db import models

from .db_connexion import mongo_db

# Create your models here.

animal_collection = mongo_db['LegendaryAnimals']


# class Animal(models.Model):
#     animal_id = models.AutoField(primary_key=True)    
#     animal_name = models.CharField(max_length=100)
#     state_name = models.CharField(max_length=100)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     date = models.DateField()
#     time = models.TimeField()
