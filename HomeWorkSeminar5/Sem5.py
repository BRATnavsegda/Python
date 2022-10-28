# import random
# import math
# from typing import List

import function_file as ff


def lets_go():
    while True:
        print("\n<<<Введите номер задачи от 1 до 4 для проверки.>>>\n"
              "\nДля выхода введите 0")
        num = ff.enter_number("> ")
        if int(num) == 1:
            print("1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""")
            for_task1()

        elif int(num) == 2:
            print("2. Создайте программу для игры с конфетами человек против человека.\n"
                  "Условие задачи: На столе лежит 2021 конфета. \n"
                  "Играют два игрока делая ход друг после друга. \n"
                  "Первый ход определяется жеребьёвкой. \n"
                  "За один ход можно забрать не более чем 28 конфет. \n"
                  "Все конфеты оппонента достаются сделавшему последний ход. \n"
                  "Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?\n"
                  "a) Добавьте игру против бота\n"
                  "b) Подумайте как наделить бота ""интеллектом""\n")
            for_task2()

        elif int(num) == 3:
            print("3. Создайте программу для игры в ""Крестики-нолики"".\n")
            for_task3()

        elif int(num) == 4:
            print("4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.\n"
                  "Входные и выходные данные хранятся в отдельных текстовых файлах.\n")
            for_task4()

        elif int(num) == 0:
            print("\nАнекдот напоследок: \n\n"
                  "Сказать что-либо, при этом никого не обидев, можно теперь только про себя.\n")

            break

        else:
            print("Введите !правильный! номер (от 1 до 5), попробуйте ещё раз...")


# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def for_task1(text="абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв"):
    print("<<<(введите строку для проверки либо нажмите Enter, если не хотите)>>>")
    user_choice = input("-->")
    if user_choice == "":
        user_choice = text
        print("Тогда используем эту строку для проверки:\n"
              "абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв\n")

    lst = ' '.join(list(filter(lambda s: 'абв' not in s, user_choice.split())))
    print(f"Результат:\n{lst}\n")
    return lst


# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

def player_turn(player=1, count=1):
    if player == 1:
        print("\nХодит первый игрок...")
    else:
        print("\nХодит второй игрок...")
    how_many = int(ff.enter_number("Сколько конфет возьмёте?-->"))

    if 0 < how_many <= 28:
        count -= how_many
        if count > 0:
            print(f"Осталось {count} ")
        else:
            end = f"Конфет больше нет" if count == 0 else f"Осталось только {count + how_many} конфет и всё же..."
            print(end)

    else:
        print("\nМожно взять только от 1 до 28 конфет")

        player_turn(player, count)
    return int(count)


def bot_calc(player=1, count=1):
    if player == 1:
        print("\nХодит первый игрок...")
        how_many = int(ff.enter_number("Сколько конфет возьмёте?-->"))

    else:
        print("\nХодит ИИ...")

        if (count - 28) < 0:
            how_many = count
            print(f"ИИ ,берет {how_many} ...")
        else:
            how_many = count % 29
            print(f"ИИ ,берет {how_many} ...")

    if 0 < how_many <= 28:
        count -= how_many
        if count > 0:
            print(f"Осталось {count} ")
        else:
            end = f"Конфет больше нет" if count == 0 else f"Осталось только {count + how_many} и всё же..."
            print(end)

    else:
        print("\nМожно взять только от 1 до 28 конфет")

        player_turn(player, count)
    return int(count)


def for_task2():
    bot_or_not = int(ff.enter_number("Играем с ИИ или живым существом?\n"
                                     "если с ИИ введите 0\n-->"))
    win1 = "\nВыиграл первый игрок и он получает все конфеты!!!"
    win2 = "\nВыиграл второй игрок и он получает все конфеты!!!"
    rand_move = int(ff.rand_num(1, 3))
    move = rand_move

    if bot_or_not != 0:
        candies = int(ff.enter_number("Сколько конфет будем разыгрывать?\nВведите количество-->"))

        while int(candies) > 0:
            candies = player_turn(1, candies) if move == 1 else player_turn(2, candies)
            if move == 1:
                move += 1
            else:
                move = 1
        if move == 1:
            print(win2)
        else:
            print(win1)
    else:
        print("По условию задачи всего конфет должно быть 2021 штука.\n"
              "но чтобы не слишком долго мучиться, я предлагаю ввести количество вручную))")
        candies = int(ff.enter_number("Сколько конфет будем разыгрывать?\nВведите количество-->"))
        # candies = 2021
        while candies > 0:
            candies = bot_calc(1, candies) if move == 1 else bot_calc(2, candies)
            if move == 1:
                move += 1
            else:
                move = 1
        if move == 1:
            print(win2)
        else:
            print(win1)


# 3. Создайте программу для игры в ""Крестики-нолики"".
def switch(player):
    if player == 1:
        player = 0
        return player
    else:
        player = 1
        return player


def check_line(line1, line2, line3, player):

    l: list[str] = ["x", "o"]
    i = 1
    print_lines(line1, line2, line3)
    while i < 10:
        turn = int(ff.enter_number(f"\nХодит игрок{player}.\n Введите число от 1 до 9:\n--> "))
        while turn < 1 or turn > 9:
            turn = int(ff.enter_number(f"\nХодит игрок{player}.\n Введите число от 1 до 9:\n--> "))

        if turn == 7 and (line1[2] == "*"):
            line1[2] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 8 and (line1[4] == "*"):
            line1[4] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 9 and (line1[6] == "*"):
            line1[6] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 4 and (line2[2] == "*"):
            line2[2] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif (turn == 5) and (line2[4] == "*"):
            line2[4] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 6 and (line2[6] == "*"):
            line2[6] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 1 and (line3[2] == "*"):
            line3[2] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 2 and (line3[4] == "*"):
            line3[4] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 3 and (line3[6] == "*"):
            line3[6] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        else:
            print('\n!!!Сюда уже кто-то походил!!!\n!!!!Сделайте ход в другую клетку!!!!\n')

        print_lines(line1, line2, line3)

    return line1, line2, line3, player


def get_winner(line1, line2, line3, player):
    l: list[str] = ['x', 'o']

    for symbol in l:
        if ((line1[2] == symbol and line1[4] == symbol and line1[6] == symbol) or
                (line2[2] == symbol and line2[4] == symbol and line2[6] == symbol) or
                (line3[2] == symbol and line3[4] == symbol and line3[6] == symbol) or
                (line1[2] == symbol and line2[2] == symbol and line3[2] == symbol) or
                (line1[4] == symbol and line2[4] == symbol and line3[4] == symbol) or
                (line1[6] == symbol and line2[6] == symbol and line3[6] == symbol) or
                (line1[2] == symbol and line2[4] == symbol and line3[6] == symbol) or
                (line1[6] == symbol and line2[4] == symbol and line3[2] == symbol)):
            print_lines(line1, line2, line3)
            print(f">>>>>>>>>>Выиграл игрок {player}<<<<<<<<<<")
            exit()
    if line1.count("*") != 0 and line2.count("*") != 0 and line3.count("*") != 0:
        return line1, line2, line3, player
    else:
        print(">>>>>>>>>>Ничья, победила дружба<<<<<<<<<<")


def print_lines(line1, line2, line3):
    up_line = list("~_______~")
    down_line = list("~_______~")
    print(*up_line)
    print(*line1)
    print(*line2)
    print(*line3)
    print(*down_line)


def for_task3():
    player = int(ff.rand_num(0, 1))
    print("\nНачинаем игру в крестики-нолики!\n"
          "Для хода необходимо ввести цифру (как на NumLock), \nкоторая соответствует позиции на поле\n"
          "Цифры соответствуют таким позициям:")

    midl_line11 = list("| 7 8 9 |")
    midl_line22 = list("| 4 5 6 |")
    midl_line33 = list("| 1 2 3 |")

    print_lines(midl_line11, midl_line22, midl_line33)

    midl_line1 = list("| * * * |")  # 2.4.6
    midl_line2 = list("| * * * |")
    midl_line3 = list("| * * * |")
    check_line(midl_line1, midl_line2, midl_line3, player)


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def encode(data_file):
    new_str = ff.read_in(data_file)
    print(f'Начальная строка\n{new_str}')
    count = 0
    result = ''

    for i in range(len(new_str)):
        count += 1
        if (i + 1) == len(new_str) or new_str[i] != new_str[i + 1]:
            result += str(count) + new_str[i]
            count = 0
    print(f'Закодированная строка\n{result}')
    return result


def decode(data_file):
    new_str = ff.read_in(data_file)
    result = ''
    count = ''
    for i in range(len(new_str)):
        if new_str[i].isdigit():
            count += new_str[i]
        else:
            result += new_str[i] * int(count)
            count = ''
    print(f'Декодированная строка\n{result}')

    return result


def for_task4():
    new_str = encode('sem5_file1.txt')
    ff.write_in('sem5_file2.txt', new_str)
    decode('sem5_file2.txt')


lets_go()
