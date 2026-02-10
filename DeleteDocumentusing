#Write a Python program to delete a document with a specific roll_no in MongoDB.

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

collection.delete_one({"roll_no":101})
print("Student Deleted")

