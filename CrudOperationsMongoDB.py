'''Perform the following operations using MongoDB:
• Display all employees in the "Finance" department.
• Update the salary of an employee with a specific id.
• Write a Python program to create a MongoDB collection Employee with fields like
Name, ID, and Salary. Insert multiple records.'''

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
emp = db["Employee"]

employee = [

    {"name":"Shubham", "id":101, "salary":800, "department":"Finance"},
    {"name":"Ritesh", "id":102, "salary":1200, "department":"IT"},
    {"name":"Jayesh", "id":103, "salary":6000, "department":"Finance"}
]

emp.insert_many(employee)
print("Employee Inserted")

#Display Employee from "finace" department

for e in emp.find({"department":"Finance"}):
    print(e)

#Update Salary of employee with specific ID

emp.update_one(
    {"id":103},
    {"$set": {"salary":9000}}

)

print("Salary Updated")

for e in emp.find():
    print(e)