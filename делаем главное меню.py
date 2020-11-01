import sys

def create_note():
    pass
def find_note():
    pass
def edit_note():
    pass
def delete_note():
    pass
def close_win():
    print("Выполнен выход из программы")
    sys.exit(0)

def print_menu():
    print ("Главное меню")
    print("1. Создать запись")
    print("2. Найти запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Выйти из программы")

menu_choice = 0
while menu_choice != 5:
    print_menu()
    menu_choice = int(input("Введите число от 1 до 5:"))
    if menu_choice == 1:
        create_note()
    elif menu_choice == 2:
        find_note()
    elif menu_choice == 3:
        edit_note()
    elif menu_choice == 4:
        delete_note()
    elif menu_choice == 5:
        close_win()
    else:
        print("Пожалуйста следуйте инструкциям")