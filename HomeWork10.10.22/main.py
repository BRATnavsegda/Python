import math


def lets_go():
    while True:
        print("\n<<<Enter the task number from 1 to 5 to check.>>>\n"
              "\nFor quit enter 0")
        num = enter_number("> ")
        if num == 1:
            print("1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, "
                  "\nи проверяет, является ли этот день выходным.")
            if_holiday()
        elif num == 2:
            print("2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n"
                  "для всех значений предикат.")
            check_predicate()
        elif num == 3:
            print("Напишите программу, которая принимает на вход координаты точки (X и Y), "
                  "\nпричём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка "
                  "\n(или на какой оси она находится).")
            quarter_number()
        elif num == 4:
            print(" 4. Напишите программу, которая по заданному номеру четверти,"
                  "\nпоказывает диапазон возможных координат точек в этой четверти (x и y).")
            quarter_coord()
        elif num == 5:
            print("5. Напишите программу, которая принимает на вход координаты двух точек "
                  "\nи находит расстояние между ними в 2D пространстве.")
            coord_in_2d()
        elif num == 0:
            print("\nАнекдот напоследок: \n\nВот чем хорош Интернет — он дает возможность высказаться каждому."
                  "\nА вот чем Интернет плох: он дает возможность высказаться каждому. ")
            break
        else:
            print("Enter the correct number, please")


# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def enter_number(message):
    number = input(message)
    try:
        float(number)

    except ValueError:
        print("Please enter the number, try again!")
        number = 0
        enter_number(message)
    return int(number)


def if_holiday():
    while True:
        day_number = enter_number("Enter the number of the day of the week from 1 to 7 \n> ")
        if day_number < 1 or day_number > 7:
            print(" \nThe number of the day of the week can be only from 1 to 7, please try again.\n")
        else:
            break
    if int(day_number) == 6 or int(day_number) == 7:
        print(f'The entered day of the week is a holiday, Congratulations\n')
    else:
        print("The entered day of the week is NOT a holiday, sorry\n")


# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

def enter_list():
    result = [input('Enter x,y,z (3 numbers) separated by a space\n> ').split()]
    return result


# def check_predicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     print(result)
#
def check_predicate():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                left = not(x or y or z)
                right = not x and not y and not z

                if left == right:
                    print(f'{x} {y} {z} -> True')
                else:
                    print(f'{x} {y} {z} -> False')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quarter_number():
    while True:
        x = enter_number("Enter the number for x coordinate\nx = ")
        y = enter_number("Enter the number for x coordinate\ny = ")
        if x == 0 or y == 0:
            print(" \nX or Y can't be equal to 0, please try again.\n")
        else:
            break
    if x > 0 and y > 0:
        print(f' \nThe quarter number for\nx = {x}\ny = {y}\nis I quarter.')
    elif x < 0 < y:
        print(f' \nThe quarter number for\nx = {x}\ny = {y}\nis II quarter.')
    elif x < 0 and y < 0:
        print(f' \nThe quarter number for\nx = {x}\ny = {y}\nis III quarter.')
    elif y < 0 < x:
        print(f' \nThe quarter number for\nx = {x}\ny = {y}\nis IV quarter.')


# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def quarter_coord():
    while True:
        num = enter_number("Enter the number of quarter:\nQuarter №  ")
        if num > 4 or num < 1:
            print(" \nQuarter can be 1, 2, 3 or 4, please try again.\n")
        else:
            break
    if num == 1:
        print(f' \nFor the quarter №{num}, point can be in the following range (x > 0;y > 0).')
    elif num == 2:
        print(f' \nFor the quarter №{num}, point can be in the following range (x < 0;y > 0).')
    elif num == 3:
        print(f' \nFor the quarter №{num}, point can be in the following range (x < 0;y < 0).')
    elif num == 4:
        print(f' \nFor the quarter №{num}, point can be in the following range (x > 0;y < 0).')


# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def coord_in_2d():
    x1 = float(enter_number("Enter x1 "))
    y1 = float(enter_number("Enter y1 "))
    x2 = float(enter_number("Enter x2 "))
    y2 = float(enter_number("Enter y2 "))
    result = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

    print(f"A ({x1},{y1}); B ({x2},{y2}) -> {round(result, 2)}")


lets_go()
