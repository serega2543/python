# Реализуйте алгоритм перемешивания списка.

import random
arr = [random.randint(0,10) for i in range(random.randint(5,10))]
print(f"Исходный список:\n{arr}")
random.shuffle(arr)
print(f"Перешивание списка:\n{arr}")