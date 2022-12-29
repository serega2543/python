# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randint

def list(n):
    list = []
    for i in range(n*2):
        list.append(randint(0, n))
    return list


n = int(input('Введите любое число: '))
numbers = list(n)
print(numbers)

new_arr=[]
for i in numbers: 
    if i not in new_arr: 
        new_arr.append(i) 

print(new_arr)

