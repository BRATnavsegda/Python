import random
import math
import function_file as ff


def lets_go():
    while True:
        print("\n<<<Введите номер задачи от 1 до 5 для проверки.>>>\n"
              "\nДля выхода введите 0")
        num = enter_number("> ")
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
                  "Гаишник останавливает нарушителя за превышение скорости. Проверил его права, \n"
                  "стpaховку и выписал парню штраф. Ну, парнишка, весь такой расстроенный, спрашивает у\n"
                  "полицейского: \n"
                  "- Товарищ лейтенант, вы не возражаете, если я вам задам вопрос?\n"
                  "- Задавайте.\n"
                  "- Вот посмотрите на все эти машины, которые мимо нас проезжают. Ведь как минимум 75%\n"
                  "  из них превышают скорость. А вы остановили именно меня? Почему?\n"
                  "- Вы когда нибудь были на рыбалке?\n"
                  "- Да.\n"
                  "- Вы всех рыб выловили?..\n")

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


def write_in(file, inp_data):
    with open(file, 'w') as data:
        data.write(inp_data)


def read_in(file):
    with open(file, 'r') as data:
        r = data.read()
        return r


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
            end = f"Конфет больше нет" if count == 0 else f"Осталось только {count+how_many} конфет и всё же..."
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

def for_task3():
    a = 0


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def for_task4():
    a = 0


lets_go()
