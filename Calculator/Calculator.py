import math
from os import close


print('1. Сложение')
print('2. Вычетание')
print('3. Умножение')
print('4. Деление')
print('5. Квадратный корень числа')
print('6. Возведение в степень')
print('7. Факториал числа')
print('8. Синус')
print('9. Косинус')
print('10. Тангенс')
print('11. Выход')

print('Введите операцию:')
oper = input()


while (oper != '11'):
    
    while True:
        try:
            x = int(input('Введите первое значение: '))
            break
        except ValueError:
            print("Извините, вы ввели не числовое значение, попробуйте снова")

    while True:
        try:
            y = int(input('Введите второе значение: '))
            break
        except ValueError:
            print("Извините, вы ввели не числовое значение, попробуйте снова")


    if oper == '1':
        print('Сложение: ', x + y)
    elif oper == '2':
        print('Вычетание: ', x - y)
    elif oper == '3':
        print('Произведение: ', x * y)
    elif oper == '4':
        if y != 0:
            print('Деление: ', x / y)
        else:
            print('Деление на ноль неосуществимо, попробуйте снова.')
    elif oper == '5':
        if (x < 0):
            print("Извините, отрицательного корня не существует")
        else:
            print('Корень X: ', math.sqrt(x))
        if (y < 0):
            print("Извините, отрицательного корня не существует")
        else:
            print("Корень Y: ", math.sqrt(y))
    elif oper == '6':
        print('Степень: ', x ** y)
    elif oper == '7':
        if (x < 0):
            print("Извините, отрицательного факториала не существует")
        else:
            print('Факториал X: ', math.factorial(x))
        if (y < 0):
            print("Извините, отрицательного факториала не существует")
        else:
            print("Факториал Y: ", math.factorial(y))
    elif oper == '8':
        print('Синус: ', math.sin(x), math.sin(y))
    elif oper == '9':
        print('Косинус: ', math.cos(x), math.cos(y))
    elif oper == '10':
        print('Тангенс: ', math.tan(x), math.tan(y))
    print('Введите операцию:')
    oper = input()
