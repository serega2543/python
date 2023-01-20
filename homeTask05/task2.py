# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def delwords(my_text):
    my_text = list(filter(lambda el: 'абв' not in el, my_text.split()))
    return " ".join(my_text)


my_text = 'dfg абвыва ываабвыва, ыващшшхАБВ - ывад абв. F<Df,dffАБВабв аа'

new_text = delwords(my_text)
print(my_text)
print(new_text)