import math


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
    
    print('Введите первое значение: ');
    x = int(input())
    print('Введите второе значение: ');
    y = int(input())
    
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
        print('Корень: ', math.sqrt(x), math.sqrt(y))
    elif oper == '6':
        print('Степень: ', x ** y)
    elif oper == '7':
        print('Факториал: ', math.factorial(x), math.factorial(y))
    elif oper == '8':
        print('Синус: ', math.sin(x), math.sin(y))
    elif oper == '9':
        print('Косинус: ', math.cos(x), math.cos(y))
    elif oper == '10':
        print('Тангенс: ', math.tan(x), math.tan(y))
    print('Введите операцию:')
    oper = input()
