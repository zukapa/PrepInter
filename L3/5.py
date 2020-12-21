import re


def change_file():
    scan_list = []
    with open('file.txt', 'r', encoding='utf-8') as fd:
        for ind, val in enumerate(fd):
            string = ''.join(re.findall(r'[a-z]', f'{val}'))
            full_string = f'{string} {string}\n'
            scan_list.append(full_string)
        fd.seek(0)
    with open('file2.txt', 'w', encoding='utf-8') as fd:
        for val in scan_list:
            fd.write(f'{val}')


change_file()
