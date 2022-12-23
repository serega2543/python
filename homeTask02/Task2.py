# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число: "))

for i in range(1, n+1):
    j=1
    res=1
    res_array=[]
    while j<=i:
        res=res*j
        j=j+1
        res_array.append(res)

print (f"{n} -> {res_array}")