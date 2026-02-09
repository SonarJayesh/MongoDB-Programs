#Implement a Python program to fetch all documents from a MongoDB collection.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["collegeDB"]
collection = db["Student"]


Students = {
    "name":"Jayesh",
    "roll_no":101,
    "marks":85
}

collection.insert_one(Students)
print("Student inserted Successfully")


for student in collection.find():
    print(student)
