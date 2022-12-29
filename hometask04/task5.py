# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


import re
import itertools


file1 = '1.txt'
file2 = '2.txt'
file_sum = 'sum.txt'

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(pol):
    pol = pol.replace('= 0', '').replace('- ', '+-')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)

    # print([tuple(x for x in j if x != 'x') for j in pol])
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol


def add_poly(*args):
    expval = sorted([(e, v) for poly in args for v, e in poly])
    return [
        (sum(v for _, v in g), e)
        for e, g in itertools.groupby(expval, key=lambda kv: kv[0])
    ]



def get_sum_pol(pol):
    new_arr = ''
    for i in pol:
        j = ''
        if i[0]>0:
            znak = '+'
            j=i[0]
        else:
            znak = '-'
            j = -i[0]

        kkk=''
        if i[1]==1:
            kkk = '*x'
        elif i[1]>1:
            kkk = f'*x^{i[1]}'

        if i[0]!=0:
            if new_arr == '':
                if i[0]>0:
                    new_arr = f'{j}{kkk}'
                else:
                    new_arr = f'-{j}{kkk}'
            else:
                new_arr = f'{new_arr} {znak} {j}{kkk}'


    return new_arr

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

# print(pol_1)
# print(pol_2)
sum_pul = add_poly(pol_1, pol_2)
param = sorted(sum_pul, key=lambda x: x[1], reverse=True)
# print(param)
res_polynomial = get_sum_pol(param)
write_to_file(file_sum, get_sum_pol(param))
print(res_polynomial)