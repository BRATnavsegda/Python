import math
import random


def lets_go():
    while True:
        print("\n<<<Введите номер задачи от 1 до 5 для проверки.>>>\n"
              "\nДля выхода введите 0")
        num = enter_number("> ")
        if int(num) == 1:
            print("1. Вычислить число Пи c заданной точностью d\n")
            for_task1()

        elif int(num) == 2:
            print("2. Задайте натуральное число N. Напишите программу, которая \n"
                  "составит список простых множителей числа N.")
            for_task2()

        elif int(num) == 3:
            print("3. Задайте последовательность цифр.  \n"
                  "Напишите программу, которая выведет список неповторяющихся элементов \n"
                  "исходной последовательности.")
            for_task3()

        elif int(num) == 4:
            print("4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов"
                  "(значения от -100 до 100) многочлена и записать в файл многочлен степени k "
                  "k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля. "
                  "Коэффициенты расставляет random, поэтому при коэффициенте 0 "
                  "просто пропускаем данную итерацию степени. Записываем результат в файл.")
            # for_task4()
            write_in('file1.txt', for_task4())
            write_in('file2.txt', for_task4())
            print("Два полученных многочлена записаны в разные файлы, на память.")

        elif int(num) == 5:
            print("5. Даны два файла, в каждом из которых находится запись многочлена. "
                  "Задача - сформировать файл, содержащий сумму многочленов.")
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


def write_in(file, inp_data):
    with open(file, 'w') as data:
        data.write(inp_data)


def read_in(file):
    with open(file, 'r') as data:
        r = data.read()
        return r


# 1. Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
#
# !!! не округлять константу math.pi


def for_task1():
    d = len(enter_number("Введите нужную точность:\nd = _"))
    my_pi = (4 / 1) - (4 / 3)
    temp = 5
    pi_math = math.pi
    for i in range(1000000):  # тут можно увеличить точность числа Пи, но будет дольше считать
        my_pi += (4 / temp)
        temp += 2
        my_pi -= (4 / temp)
        temp += 2
    print(f'Пи полученная с помощью библиотеки math --> {pi_math}')
    print(f'Пи которую мы вычислили --> {my_pi}')
    print(f'Уточненное число --> {str(my_pi)[:d]}')


# 2. Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.


def for_task2():
    user_num = int(enter_number('Введите натуральное число:\n-->'))
    i = 2
    result = []
    temp = user_num
    while i <= temp:
        if temp % i == 0:
            result.append(i)
            temp //= i
            i = 2
        else:
            i += 1
    print(f"Список простых множителей числа {user_num}:")
    print(*result)


# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


def for_task3():
    print(f"Случайная последовательность цифр:")
    new_list = [rand_num(1, 10) for i in range(1, 10)]
    print(*new_list)
    result = []
    for i in range(len(new_list)):
        cnt = new_list.count(new_list[i])
        if cnt == 1:
            result.append(new_list[i])
        else:
            continue
    print(f"\nНеповторяющиеся элементы:")
    print(*result)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k.
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени.
# Записываем результат в файл.
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


def for_task4():
    user_num = int(enter_number("Введите максимальную степень многочлена (от 1 до 10):\nk = "))

    if user_num < 1 or user_num > 10:
        print("Не вводите степень больше 10 или меньше 1, пробуем ещё раз...")
        return for_task4()

    result = []
    result2 = ""

    while user_num != 0:
        num = rand_num()
        if user_num == 1:
            temp = "%dx + " % num
            result.append(temp)
        elif num == 1:
            temp = "x^%d + " % user_num
            result.append(temp)
        elif num != 0:
            temp = "%dx^%d + " % (num, user_num)
            result.append(temp)
        else:
            continue
        user_num -= 1

    for i in range(len(result)):
        result2 += str(result[i])
    result2 = result2[:-2]
    result2 += '= 0'

    print(result2)

    return result2


def for_task5():
    many_xy1 = read_in("file1.txt")
    many_xy2 = read_in("file2.txt")
    a = many_xy1[:-3].replace(" ", "").replace("^", "").split("+")
    b = many_xy2[:-3].replace(" ", "").replace("^", "").split("+")
    print(a, b)
    result = []
    if len(a) < len(b):
        for i in range(len(b)):
            temp1 = 'x' + str(i)
            if temp1 in b:



    elif len(a) == len(b):
        for i in range(len(b)):

    else:




for_task5()

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0




# В конец генератора можно добавлять конструкцию if. Например, надо из строки извлечь все цифры:
#
# >>> a = "lsj94ksd231 9"
# >>> b = [int(i) for i in a if '0'<=i<='9']
# >>> b
# [9, 4, 2, 3, 1, 9]

# 1)
# path = "sem5.txt"
# f = open(path, "r")
# data = f.read().split()
# print(*data)
# f.close()

# data = list(map(int, data))
# print(data)
# for i in range(len(data) - 1):
#     if data[i] + 1 == data[i + 1]:
#         continue
#     else:
#         print(data[i] + 1)

# >>>>>>>>> open('file.txt', 'w', encoding='utf-8') cp1251


# lets_go()
