import re


def comp_number(number):
    if type(number) != int and type(number) != float:
        print(f'Введено не целое и не вещественное число')
    if type(number) == int:
        print(f'Число {number} целое')
    if type(number) == float:
        print(f'Число {number} вещественное')
        left = re.sub('[.]+.*', '', f'{number}')
        right = re.sub('.*[.]', '', f'{number}')
        if left == right:
            print(f'Левая и правая части совпадают')
        else:
            print(f'Левая и правая части не совпадают')


comp_number(11.11)
