import sqlite3
conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()


def key_pair_reception(str):
    global field
    print("\nВыберите по какому критерию произвести " + str + "  (от 1 до 3)")
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
    keyword = input("\nВведите значение для  поля  ")
    keypair = field + "='" + keyword + "'"
    return keypair

def findcontacts():
    s = key_pair_reception('поиск')
    cur.execute('SELECT id, surname, name, phone_number FROM phonebook WHERE ' + s + ' ORDER BY id')
    results = cur.fetchall()
    not_found = []
    if results == not_found:
        print("Поиск не дал результатов")
    else:
        print(results)
    return results

def choose():
    chosen_contact=int(input("Введите id контакта в котором необходимо внести изменения: "))
    cur.execute("SELECT name, surname, phone_number FROM phonebook WHERE id LIKE {}".format(chosen_contact))
    conn.commit()
    return chosen_contact

def editcontacts():
    s = findcontacts()
    c = choose()
    u = key_pair_reception('обновление')
    if s is not None:
        sql = ("UPDATE phonebook SET {}  WHERE {} LIKE '%{}%'".format(u, s, c))
        cur.execute(sql)
        conn.commit()
        print("Запись изменена.\n")
