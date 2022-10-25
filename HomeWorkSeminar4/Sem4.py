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
            print("4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов\n"
                  "(значения от -100 до 100) многочлена и записать в файл многочлен степени k \n"
                  "k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля. \n"
                  "Коэффициенты расставляет random, поэтому при коэффициенте 0 \n"
                  "просто пропускаем данную итерацию степени. Записываем результат в файл.\n")
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


# 1. Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
#
# !!! не округлять константу math.pi


def for_task1():
    d = len(enter_number("Введите нужную точность:\nd = "))
    my_pi = (4 / 1) - (4 / 3)
    temp = 5
    pi_math = math.pi
    for i in range(d**10):  # тут можно увеличить точность числа Пи, но будет дольше считать
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
    new_list = [rand_num(1, 10) for i in range(1, 20)]
    print(*new_list)
    result = list(filter(lambda n: new_list.count(n) == 1, new_list))  # в Дискорде сократили моё решение

    # for i in range(len(new_list)):
    #     cnt = new_list.count(new_list[i])
    #     if cnt == 1:
    #         result.append(new_list[i])
    #     else:
    #         continue
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


# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0


def for_task5():
    many_xy1 = str_in_dict(read_in("file1.txt"))
    many_xy2 = str_in_dict(read_in("file2.txt"))

    if len(many_xy2) >= len(many_xy1):
        for e in many_xy1.keys():
            many_xy2[e] = int(many_xy2.get(e, 0)) + int(many_xy1[e])
        sum_dict = dict_in_str(many_xy2)

    else:
        for e in many_xy2.keys():
            many_xy1[e] = int(many_xy1.get(e, 0)) + int(many_xy2[e])
        sum_dict = dict_in_str(many_xy1)

    print(f'\nМногочлен из первого файла:\n{read_in("file1.txt")}')
    print(f'\nМногочлен из второго файла:\n{read_in("file2.txt")}')
    print(f'\nСумма многочленов:\n{sum_dict}')
    write_in('file3.txt', sum_dict)


def dict_in_str(dict1):
    result = ''
    for i in dict1:
        temp = f'{dict1[i]}x^{i} + '
        result += temp

    result = result[:-5].replace('+ -', '- ')
    result += ' = 0'
    return result


def str_in_dict(str1):

    str2 = str1[:-3].replace(" ", "").replace("^", "").split("+")

    dict1 = {}
    for i in range(len(str2)):
        temp = str2[i].split('x')
        if temp[1] == '':
            temp[1] = 1
        elif temp[1] == '-':
            temp[1] = -1
        dict1[temp[1]] = temp[0]

    return dict1


# lets_go()
