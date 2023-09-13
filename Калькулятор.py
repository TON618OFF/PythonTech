import math

print('Введите операцию: ')
oper = input()
print('Введите первое значение: ')
x = int(input())
print('Введите второе значение: ')
y = int(input())

summ = x + y
diff = x - y
mult = x * y
div = x / y
deg = x ** y
sqrt = x or y ** 0.5

if oper != '+' or 'сложение':
    print(summ)
else:
    print(diff)
if oper != '*' or 'умножение':
    print(mult)
else:
    print(div)
if oper != '**' or 'степень':
    print(deg)
else:
    print(sqrt)