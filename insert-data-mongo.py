from pymongo import MongoClient
from datetime import datetime

# MongoDB connection URI
MONGO_URI = "mongodb://root:root@localhost:27017/?authSource=admin"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["student_records"]

# students data
students = [
    {"student_id": "20231230", "name": "Zara Cooper", "department": "Computer Science", "cgpa": 3.74, "graduation_year": 2025},
    {"student_id": "20231231", "name": "Alice Johnson", "department": "Computer Science", "cgpa": 3.85, "graduation_year": 2025},
    {"student_id": "20231232", "name": "Benjamin Smith", "department": "Electrical Engineering", "cgpa": 3.67, "graduation_year": 2024},
    {"student_id": "20231233", "name": "Chloe Davis", "department": "Mechanical Engineering", "cgpa": 3.52, "graduation_year": 2025},
    {"student_id": "20231234", "name": "Daniel Brown", "department": "Civil Engineering", "cgpa": 3.91, "graduation_year": 2023},
    {"student_id": "20231235", "name": "Emily Wilson", "department": "Computer Science", "cgpa": 3.78, "graduation_year": 2026},
    {"student_id": "20231236", "name": "Frank Miller", "department": "Physics", "cgpa": 3.43, "graduation_year": 2024},
    {"student_id": "20231237", "name": "Grace Taylor", "department": "Mathematics", "cgpa": 3.95, "graduation_year": 2025},
    {"student_id": "20231238", "name": "Henry AComputer Sciencenderson", "department": "Computer Science", "cgpa": 3.64, "graduation_year": 2023},
    {"student_id": "20231239", "name": "Isabella Thomas", "department": "Electrical Engineering", "cgpa": 3.72, "graduation_year": 2025},
    {"student_id": "20231240", "name": "Jack Martinez", "department": "Biochemistry", "cgpa": 3.59, "graduation_year": 2024},
    {"student_id": "20231241", "name": "Katherine Moore", "department": "Civil Engineering", "cgpa": 3.41, "graduation_year": 2026},
    {"student_id": "20231242", "name": "Liam Jackson", "department": "Architecture", "cgpa": 3.88, "graduation_year": 2024},
    {"student_id": "20231243", "name": "Mia White", "department": "Mechanical Engineering", "cgpa": 3.56, "graduation_year": 2025},
    {"student_id": "20231244", "name": "Noah Harris", "department": "Environmental Science", "cgpa": 3.66, "graduation_year": 2023},
    {"student_id": "20231245", "name": "Olivia Clark", "department": "Computer Science", "cgpa": 3.93, "graduation_year": 2026},
    {"student_id": "20231246", "name": "Patrick Lewis", "department": "Physics", "cgpa": 3.51, "graduation_year": 2025},
    {"student_id": "20231247", "name": "Quinn Walker", "department": "Mathematics", "cgpa": 3.77, "graduation_year": 2024},
    {"student_id": "20231248", "name": "Ruby Hall", "department": "Electrical Engineering", "cgpa": 3.82, "graduation_year": 2026},
    {"student_id": "20231249", "name": "Samuel Allen", "department": "", "cgpa": 2.42, "graduation_year": 2023}
]


# Insert into collections
db.students.insert_many(students)
#db.sales.insert_many(sales)

print("Data inserted successfully.")
