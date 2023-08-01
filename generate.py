import sqlite3
from faker import Faker
import random

# Функція для створення бази даних та наповнення випадковими даними
def create_and_populate_database():
    fake = Faker()
    connection = sqlite3.connect('hw_6\my_database.db')
    cursor = connection.cursor()

    # Створення таблиць
    cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            group_id INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE groups (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE teachers (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE subjects (
            id INTEGER PRIMARY KEY,
            name TEXT,
            teacher_id INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE grades (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER,
            date TEXT
        )
    ''')

    # Наповнення таблиць випадковими даними
    groups = ['Group A', 'Group B', 'Group C']
    teachers = [fake.name() for _ in range(5)]
    subjects = [fake.word() for _ in range(8)]

    for group in groups:
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (group,))
    
    for teacher in teachers:
        cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher,))

    for subject in subjects:
        teacher_id = random.randint(1, len(teachers))
        cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

    for _ in range(30):
        name = fake.name()
        group_id = random.randint(1, len(groups))
        cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))

    students_ids = [i for i in range(1, 31)]
    subjects_ids = [i for i in range(1, 9)]

    for student_id in students_ids:
        for subject_id in subjects_ids:
            grade = random.randint(70, 100)
            date = fake.date_between(start_date='-90d', end_date='today')
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                           (student_id, subject_id, grade, date))

    connection.commit()
    cursor.close()
    connection.close()

# Виклик функції для створення бази даних та наповнення її випадковими даними
create_and_populate_database()
