# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

dayNumber = int(input('Введите номер дня недели:'))

if dayNumber==6 or dayNumber==7:
    print(f'{dayNumber} -> да')
elif dayNumber>7 or dayNumber<1:
    print('Ошибка! Некорректный номер дня недели')
    dayNumber
else: print(f'{dayNumber} -> нет')