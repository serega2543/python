# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Точка A:')
xA = int(input('Введите значение Х:'))
yA = int(input('Введите значение Y:'))

print('Точка B:')
xB = int(input('Введите значение Х:'))
yB = int(input('Введите значение Y:'))

AB = round(((xB-xA)**2 + (yB-yA)**2)**(1/2), 2)
print (AB)
