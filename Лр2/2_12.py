from math import pi
#ввод длины кубической ёмкости
a=float(input('Введите длину кубической ёмкости: '))
#ввод высоты цилиндрической ёмкости
h=float(input('Введите высоту цилиндрической ёмкости: '))
#ввод радиуса кубической ёмкости
r=float(input('Введите радиус цилиндрической ёмкости: '))
#ввод объёма жидкости M
m=float(input('Введите объём жидкости(л^3): '))
v1 = a**3
v2 = pi*(r**2)*h
if m>=v1:
    if m>=v1+v2: print('Заполнит обе')
    else: print('Заполнит первую')
else: print('Заполнит вторую')