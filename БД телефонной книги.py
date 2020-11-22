
import sys
import sqlite3
import createmodule
import findmodule
import editmodule


def delete_note():
    pass
def displaybook():
    cur.execute("SELECT id, surname, name, phone_number FROM phonebook ORDER BY id")
    results = cur.fetchall()
    print(results)

def close_win():
    print("Выполнен выход из программы")
    sys.exit(0)

def print_menu():
    print ("Главное меню")
    print("1. Создать запись")
    print("2. Найти запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Показать все записи")
    print("6. Выйти из программы")


conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS phonebook(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   surname TEXT,
   phone_number INT,
   comment TEXT);
""")
conn.commit()

menu_choice = 0
while menu_choice != 6:
    print_menu()
    menu_choice = int(input("Введите число от 1 до 5:"))
    if menu_choice == 1:
        createmodule.create_note()
    elif menu_choice == 2:
        findmodule.findcontacts()
    elif menu_choice == 3:
        editmodule.edit_note()
    elif menu_choice == 4:
        delete_note()
    elif menu_choice == 5:
        displaybook()
    elif menu_choice == 6:
        close_win()
    else:
        print("Пожалуйста следуйте инструкциям")
