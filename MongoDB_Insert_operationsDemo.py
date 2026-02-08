# Write a Python program to create a MongoDB collection named Students with fields like name, roll_no, and marks. Insert data into it.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collageDB"]
collection = db["students"]

Students = {
    "name":"Jayesh",\
    "roll_no":101,
    "marks":85
}

collection.insert_one(Students)
print("Student inserted Successfully")
