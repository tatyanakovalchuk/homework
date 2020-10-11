txt = input("Введите строку:")
def myfuction(txt):
    for i in txt:
        x = input("Введите символ, который Вы хотите найти в строке:")
        count=txt.count(x)
        print("Количество символов в строке: "+str(count))

myfuction(txt)
