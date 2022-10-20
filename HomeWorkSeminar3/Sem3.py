import random


def lets_go():
    while True:
        print("\n<<<Введите номер задачи от 1 до 5 для проверки.>>>\n"
              "\nДля выхода введите 0")
        num = enter_number("> ")
        if int(num) == 1:
            print("1. Задайте список из нескольких чисел.\n"
                  " Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")
            for_task1()

        elif int(num) == 2:
            print("2. Напишите программу, которая найдёт произведение пар чисел списка. \n"
                  "Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
            for_task2()

        elif int(num) == 3:
            print("3. Задайте список из вещественных чисел. \n"
                  "Напишите программу, которая найдёт разницу между \n"
                  "максимальным и минимальным значением дробной части элементов.")
            for_task3()

        elif int(num) == 4:
            print(" 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.")
            for_task4()

        elif int(num) == 5:
            print("5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")
            for_task5()

        elif int(num) == 0:
            print("\nАнекдот напоследок: \n\n"
                  "1 монитор — обычный программист, 2 монитора — продвинутый программист, \n"
                  "3 монитора — системный программист, 4 монитора — охранник.\n")

            break

        else:
            print("Введите !правильный! номер (от 1 до 5), попробуйте ещё раз...")


def rand_num(start=-100, finish=100):
    num = random.randint(start, finish)
    return num


def enter_number(message):
    number = input(message)
    try:
        float(number)

    except ValueError:
        print("Введите число, попробуйте ещё раз!")
        return enter_number(message)
    return number


def enter_list(message):
    user_list = input(message).split()
    return user_list


# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def for_task1():
    user_list = []
    rand = rand_num(5, 11)
    for n in range(rand):
        user_list.append(rand_num())
    print(f'\nЭто ваш список:\n{user_list}')

    i = 1
    result = 0
    print("На нечётных позициях находятся элементы: ", sep="", end="")
    while i < len(user_list):
        result += int(user_list[i])
        print(f'--> {user_list[i]}', sep=" ", end=" ")
        i += 2
    print(f'\nСуммой элементов стоящих на нечётных позициях вашего списка будет: {result}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def for_task2():
    user_list = []
    rand = rand_num(4, 6)
    for n in range(rand):
        user_list.append(rand_num(-10, 10))
    print(f'\nЭто ваш список:\n{user_list}')

    pos_list = []
    len_list = len(user_list)

    if len_list % 2 == 0:
        for i in range(int(len_list / 2)):
            pos_list.append(user_list[i] * user_list[-i - 1])

    else:
        for i in range(int(len_list / 2 + 1)):
            pos_list.append(user_list[i] * user_list[-i - 1])

    print(f'\nСписок произведений пар чисел:\n{pos_list}')


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def for_task3():
    user_list = enter_list("\nЗадайте список из нескольких вещественных чисел, разделённых пробелами:\n>")
    # [1.1, 1.2, 3.1, 5, 10.01]
    print(f'Это ваш список: {user_list}')
    min_el = max_el = 0.0

    for i in range(len(user_list)):
        temp = float(user_list[i])

        temp %= 1
        if temp > max_el:
            max_el = temp
        elif temp < min_el:
            min_el = temp

    result = int((max_el - min_el) * 100) / 100

    print(f'Разница между максимальным и минимальным значением \nдробной части элементов-->{result}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def for_task4():
    user_num = abs(int(enter_number("Введите десятичное число для преобразования в двоичное:\n-->")))
    temp = user_num
    result = []

    while temp != 0:
        result.append(temp % 2)
        temp = int(temp / 2)

    result.reverse()
    print(f'Число {user_num} в двоичной системе счисления: {"".join(map(str, result))}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
# (Fn = F(n+2)−F(n+1).
# Они также могут быть определены по формуле F−n = (−1)n+1Fn..)

def for_task5():
    user_num = 8  # abs(int(enter_number("Введите число для составления списка:\n-->")))
    if user_num == 0:
        print([0])

    else:
        res = [0, 1]
        negative_res = [1, 0]

        for i in range(2, user_num + 1):
            res.append(res[i - 1] + res[i - 2])
            negative_res.insert(0, negative_res[1] - negative_res[0])

        del(res[0])
        negative_res.extend(res)
        print(negative_res)


lets_go()


