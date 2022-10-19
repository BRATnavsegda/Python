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

        elif int(num) == 3:
            print("3. Задайте список из вещественных чисел. \n"
                  "Напишите программу, которая найдёт разницу между \n"
                  "максимальным и минимальным значением дробной части элементов.")

        elif int(num) == 4:
            print(" 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.")

        elif int(num) == 5:
            print("5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

        elif int(num) == 0:
            print("\nАнекдот напоследок: \n\n"
                  "Instagram был заблокирован в России.\n"
                  "Количество пользователей из Нидерландов увеличилось на 59 млн.\n")
            break

        else:
            print("Введите !правильный! номер (от 1 до 5), попробуйте ещё раз...")

def rand_num(start = -100, finish = 100):
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
    user_list = []  # enter_list("Задайте список из нескольких чисел, разделённых пробелами:\n>")
    rand = rand_num(5, 11)
    for n in range(rand):
        user_list.append(rand_num())
    i = 1
    result = 0
    print(f'\nЭто ваш список:\n{user_list}')
    print("На нечётных позициях находятся элементы: ", sep="", end="")
    while i < len(user_list):
        result += int(user_list[i])
        print(f'-->{user_list[i]}', sep=" ", end=" ")
        i += 2
    print(f'\nСуммой элементов стоящих на нечётных позициях вашего списка будет: {result}')


for_task1()




# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
#
#
#
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
#
#
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#
#
#
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
# (Fn = F(n+2)−F(n+1).
# Они также могут быть определены по формуле F−n = (−1)n+1Fn..)


