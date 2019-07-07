
# import csv
# with open('data.csv', 'r') as fdr:
#     students = csv.reader(fdr)
#     for student in students:
#         print(student)

import csv

single_student = ['Sana', 'AI', '3-6']
students = [
    ['Sana', 'AI', '3-6'],
    ['Sana', 'AI', '3-6'],
    ['Sana', 'AI', '3-6'],
    ['Sana', 'AI', '3-6'],
    ['Sana', 'AI', '3-6'],
    ['Sana', 'AI', '3-6'],

]
with open('data.csv','w', newline='') as fdes:
    writer = csv.writer(fdes, delimiter = ',')
    for student in students:
        writer.writerow(student)