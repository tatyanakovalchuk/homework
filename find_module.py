
import sqlite3
conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()


def search():
    print("\nВыберите по какому критерию произвести поиск (от 1 до 3)")
    print("1. Имя")
    print("2. Фамилия")
    print("3. Номер телефона")
    print("0. Возврат в главное меню")
    n = int(input("ВВедите выбраное число: "))
    if n == 1:
        field = "name"
    elif n == 2:
        field = "surname"
    elif n == 3:
        field = "phone_number"
    elif n == 0:
        return None
    else:
        print("Пожалуйста следуйте инструкциям")
    keyword = input("\nНайти: ")
    keypair = field + "='" + keyword + "'"
    return keypair


def findcontacts():
    s = search()
    cur.execute('SELECT surname, name, phone_number FROM phonebook WHERE ' + s + ' ORDER BY surname')
    results = cur.fetchall()
    not_found = []
    if results == not_found:
        print("Поиск не дал результатов")
    else:
        print(results)

findcontacts()