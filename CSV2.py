# import csv

# with open ("students.csv", "w", newline = "") as f:
#     data_handler = csv.writer(f,delimiter = ",")
#     data_handler.writerow(["Name", "Age", "RollNo"])
#     data_handler.writerow(["Sana", "25", "12345"])
#     data_handler.writerow(["Hina", "24", "23456"])
#     data_handler.writerow(["Mubashshir", "24", "56788"])

# with open("students.csv", "r") as f:
#     data_handler = csv.reader(f)
#     for data in data_handler:
#         print(data)

import csv

with open ("students.csv", "a", newline = "") as f:
    data_handler = csv.writer(f,delimiter = ",")
    name = input("Enter name of student")
    age = input("Enter name of student")
    rollno = input("Enter name of student")
    data_handler.writerow([name,age,rollno])