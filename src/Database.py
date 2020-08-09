import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["Database"]

print(client.list_database_names())