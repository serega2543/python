# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def list(n):
    list = []
    for i in range(n):
        list.append(round(random.uniform(0, n), 2))
    return list


n = int(input('Введите число N: '))
numbers = list(n)
# print(numbers)

diff = round(max(numbers) - min(numbers), 2)
print(f"{numbers} => {diff}")


# new_arr = []
# for i in range(int(len(numbers)/2)):
#     new_arr.append(numbers[i]*numbers[len(numbers)-i-1])
# if (len(numbers) % 2 != 0):
#     i = int(len(numbers)/2)
#     new_arr.append(numbers[i]*numbers[i])
# print(f"{numbers} -> {new_arr}")
