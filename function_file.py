import random
import math


def rand_num(start=-100, finish=100):  # получить случайное число
    num = random.randint(start, finish)
    return num


def enter_number(message):  # ввести цифру с клавиатуры
    number = input(message)
    try:
        float(number)

    except ValueError:
        print("Введите число, попробуйте ещё раз!")
        return enter_number(message)
    return number


def enter_list(message):  # ввести список с клавиатуры через пробел
    user_list = input(message).split()
    return user_list


def write_in(file, input_data):  # записать в файл
    with open(file, 'w') as data:
        data.write(input_data)


def read_in(file):  # считать из файла
    with open(file, 'r') as data:
        r = data.read()
        return r


def sum_dict(dict1, dict2):  # сложение словарей {1: 10, 2: 20} + {1: 10, 2: 20}
    for e in dict2.keys():   # = {1: 20, 2: 40}
        dict1[e] = int(dict1.get(e, 0)) + int(dict2[e])


# !!!!сделать ехе файл!!!

# Открыть командную строку windows
# Установить pyinstaller

# pip install pyinstaller

# Затем перейти в папку с Вашим файлом .py в командной строке (при помощи команды cd)
# Запустить команду pyinstaller не забудьте указать имя вашего скрипта

# pyinstaller --onefile <your_script_name>.py

# Всё - у вас в папке появится папка src и там будет .exe файл.


# Открыть командную строку windows
# Установить pyinstaller

# pip install pyinstaller

# Затем перейти в папку с Вашим файлом .py в командной строке (при помощи команды cd)
# Запустить команду pyinstaller не забудьте указать имя вашего скрипта

# pyinstaller --onefile <your_script_name>.py

# Всё - у вас в папке появится папка src и там будет .exe файл.


