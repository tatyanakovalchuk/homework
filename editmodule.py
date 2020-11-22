import sqlite3
import findmodule
conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

def search():
    findmodule.findcontacts()

def choose():
    chosen_contact=int(input("Введите id контакта в котором необходимо внести изменения: "))
    cur.execute("SELECT name, surname, phone_number FROM phonebook WHERE id LIKE {}".format(chosen_contact))
    conn.commit()
    return chosen_contact

def update():
    print("\nВыберите по какому критерию произвести обновление (от 1 до 3)")
    print("1. Имя")
    print("2. Фамилия")
    print("3. Номер телефона")

    n = int(input("ВВедите выбраное число: "))
    if n == 1:
        field = "name"
    elif n == 2:
        field = "surname"
    elif n == 3:
        field = "phone_number"
    else:
        print("Пожалуйста следуйте инструкциям")
    keyword = input("\nЗаменить на: ")
    keypair = field + "='" + keyword + "'"
    return keypair

def editcontacts():
    s = search()
    c = choose()
    u = update()
    if s != None:
        sql = ("UPDATE phonebook SET {}  WHERE {} LIKE '%{}%'".format(u, s, c))
        cur.execute(sql)
        conn.commit()
        print("Запись изменена.\n")
