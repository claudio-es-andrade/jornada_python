from pymongo import MongoClient

client = MongoClient("mongodb://cla:cla@mongo:27017/")

db = client.dio_live

trends_collection = db.trends
