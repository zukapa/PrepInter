import os
import re


def name_file(path):
    path = os.path.basename(path)
    return re.sub(r'[.]+.*', '', f'{path}')


print(name_file("C:\\Users\\Public\\file.txt"))
