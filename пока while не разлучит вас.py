a=int(input("Введите число A:"))
b=int(input("Введите максимальное значение цикла:"))
c=int(input("Введите шаг увеличения цикла:"))
def my_function(a,b,c):
    i=a
    while i<b:
        i += c
        if i<b:
            print("Значение :"+str(i)+ " Пока что нет")
        elif i>=b:
         print("Дождались! "+"A="+ str(i))

my_function(a,b,c)

