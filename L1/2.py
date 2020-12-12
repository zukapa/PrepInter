from pathlib import *


def print_directory_contents(sPath):
    command = Path(sPath)
    for child in command.glob("**/*"):
        print(child)


print_directory_contents('C:\\Users\\Public')
