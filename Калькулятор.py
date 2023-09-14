import math

print('Введите операцию (+,-,*,/,корень,степень,!, sin, cos, tg: ')
oper = input()
print('Введите первое значение: ')
x = int(input())
print('Введите второе значение: ')
y = int(input())

while oper == '+':
    print('Сложение: ', x + y)
    break
while oper == '-':
    print('Сложение: ', x - y)
    break
while oper == '*':
    print('Произведение: ', x * y)
    break
while oper == '/':
    print('Деление: ', x / y)
    if y == 0:
        break
while oper == 'корень':
    print('Корень: ', math.sqrt(x), math.sqrt(y))
    break
while oper == 'степень':
    print('Степень: ', x ** y)
    break
while oper == '!':
    print('Факториал: ', math.factorial(x), math.factorial(y))
    break
while oper == 'sin':
    print('Синус: ', math.sin(x), math.sin(y))
    break
while oper == 'cos':
    print('Косинус: ', math.cos(x), math.cos(y))
    break
while oper == 'tg':
    print('Тангенс: ', math.tan(x), math.tan(y))
    break


