# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

input_text = input("Введите число: ")
modify_text = str(input_text).replace('.', '')
modify_text = str(modify_text).replace(',', '')
modify_text = int(modify_text)
if modify_text < 0:
    modify_text *= -1


def sum_num(num):
    sum = 0
    while (num > 9):
        sum = int(sum + num % 10)
        num = int(num / 10)
    sum = sum + num
    return sum


print(f'{input_text} -> {sum_num(modify_text)}')
