import sqlite3

# Функція для виконання SQL-запиту з файлу та виведення результатів

def execute_query_from_file(filename):
    with open(filename, 'r') as file:
        query = file.read()

    connection = sqlite3.connect('hw_6\my_database.db')
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # Виведення результатів
    for row in results:
        print(row)

    cursor.close()
    connection.close()

# Виконуємо SQL-запити з файлів
execute_query_from_file('hw_6\query_1.sql')
execute_query_from_file('hw_6\query_2.sql')
execute_query_from_file('hw_6\query_3.sql')
execute_query_from_file('hw_6\query_4.sql')
execute_query_from_file('hw_6\query_5.sql')
execute_query_from_file('hw_6\query_6.sql')
execute_query_from_file('hw_6\query_7.sql')
execute_query_from_file('hw_6\query_8.sql')
execute_query_from_file('hw_6\query_9.sql')
execute_query_from_file('hw_6\query_10.sql')

# Виконуємо складне завдання 
execute_query_from_file('hw_6\query_11_hard.sql')
execute_query_from_file('hw_6\query_12_hard.sql')