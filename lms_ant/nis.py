import json
import csv

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []
TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]

def print_student(student):
    for field in student:
        print(' '.join(field.capitalize().split('_')),":", '\t', student[field])
    print('\n')

#######################################################################################

def print_students_list():
    '''Call print_student() for every student in STUDENTS'''
    for student in STUDENTS:
            print_student(student)

def dump_csv():
    with open('data\\student_data.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=student_fields)
        writer.writeheader()
        for student in STUDENTS:
            writer.writerow(student)

def load_csv(file_path='data\\student_data.csv'):
    with open(file_path, 'r') as read_file:
    	reader = csv.DictReader(read_file)
    	for row in reader:
    		STUDENTS.append(row)
#        STUDENTS.extend(list(csv.load(read_file)))  

ACTIONS = {
    'add': add_student,
    'avg_age': calculate_avg_age,
    'load': load_students,
    'print': print_students_list,
    'dump': dump_studens,
    'dump_csv': dump_csv,
    'load_json': load_from_json,
    'load_csv': load_csv
}




while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
            ACTIONS.get(action)()
        else:
            break      			  	