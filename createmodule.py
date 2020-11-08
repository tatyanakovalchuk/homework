import sys
import sqlite3

def create_note():
    while True:
        name = input("Введите имя: ")
        if len(name) != 0:
            break
        else:
            print("Пожалуйста, введите имя")
    while True:
        surname = input("Введите фамилию: ")
        if len(surname) != 0:
            break
        else:
            print("Пожалуйста, введите фамилию")
    while True:
        phone_number = input("Введите номер телефона:  (только цифры, 10 шт.): ")
        if not phone_number.isdigit():
            print("Пожалуйста, введите только цифры")
            continue
        elif len(phone_number) != 10:
            print("Пожалуйста, введите 10-ти значный немер телефона, без запятых, пробелов, дефисов")
            continue
        else:
            break
    while True:
        comment = input("Введите комментарий: ")
        if len(comment) != 0:
            break
        else:
            print("Пожалуйста, введите комментарий")

    print("Новая запись успешно добавлена")

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                name text NOT NULL,
                surname text,
                phone_number text)''');
conn.commit()
create_note()