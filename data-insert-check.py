from pymongo import MongoClient

MONGO_URI = "mongodb://root:root@localhost:27017/?authSource=admin"
client = MongoClient(MONGO_URI)
db = client["student_records"]

for doc in db.students.find():
    print(doc)
    