from pymongo import MongoClient

# Connection URI
uri = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6'
client = MongoClient(uri)

# Database and collection names
db_name = 'legendaryAnimals'
collection_name = 'Animals'

mongo_db = client[db_name]