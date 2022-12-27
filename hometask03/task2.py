# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def list(n):
    list = []
    for i in range(n):
        list.append(randint(0, n))
    return list


n = int(input('Введите число N: '))
numbers = list(n)
# print(numbers)


new_arr = []
for i in range(int(len(numbers)/2)):
    new_arr.append(numbers[i]*numbers[len(numbers)-i-1])
if (len(numbers) % 2 != 0):
    i = int(len(numbers)/2)
    new_arr.append(numbers[i]*numbers[i])
print(f"{numbers} -> {new_arr}")
