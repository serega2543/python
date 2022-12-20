# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

numPlane = int(input('Введите номер четверти:'))

if numPlane == 1:
    print('x(0;+oo), y(0;+oo)')
elif numPlane == 2:
    print('x(0;-oo), y(0;+oo)')
elif numPlane == 3:
    print('x(0;-oo), y(0;-oo)')
elif numPlane == 4:
    print('x(0;+oo), y(0;-oo)')
