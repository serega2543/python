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

# Решение через enumerate
sum=0
for i, el in enumerate(numbers):
    if i % 2 != 0:
        sum += el
        print(i, el)
print(f"Сумма нечетных элементов: {sum}")

# Решение через range
sum=0
for i in range(1, len(numbers), 2):
    print(i, numbers[i])
    sum += numbers[i]
print(f"Сумма нечетных элементов: {sum}")

