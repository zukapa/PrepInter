import random
import os


def create_file():
    number = [str(ind) for ind in range(0, 10)]
    text = [chr(ind) for ind in range(ord('a'), ord('z'))]
    random_number = [''.join(random.sample(number, 3)) for _ in range(0, 10)]
    random_text = [''.join(random.sample(text, 9)) for _ in range(0, 10)]
    zip_list = list(zip(random_number, random_text))
    if os.path.exists('file.txt') is True:
        print('Файл уже существует!')
    else:
        with open('file.txt', 'w+', encoding='utf-8') as fd:
            for ind, val in enumerate(zip_list):
                for index, value in enumerate(val):
                    fd.write(f'{value} ')
                fd.write(f'\n')
            fd.seek(0, 0)
            read_file(fd)


def read_file(fd):
    print(fd.read())


create_file()
