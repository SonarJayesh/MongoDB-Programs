from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
DB = client["MyDB"]
mycoll = DB["Collection"]
print("Connection Successful...!")

one = {
    "Name":"Jayesh",
    "Age":21,
    "Class":"MCA"
    }
mycoll.insert_one(one)
print("Date Inserted...!")