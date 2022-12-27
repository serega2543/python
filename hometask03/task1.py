# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def list(n):
    list = []
    for i in range(n):
        list.append(randint(0, n))
    return list


n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)


# even = True
# summ = 0
# for i in numbers:
#     # print(even)
#     if even == False:
#         summ = summ + int(i)
#         # print(i)
#         even = True
#     else:
#         even = False
# print(f"Сумма нечетных элементов: {summ}")


summ1 = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        summ1 = summ1 + numbers[i]
print(f"\nСумма нечетных элементов: {summ1}")
