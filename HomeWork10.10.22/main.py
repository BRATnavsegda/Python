def lets_go():
    while True:
        print("\nEnter the task number from 1 to 5 to check.\n"
              "\nFor quit enter 0")
        num = enter_number("> ")
        if num == 1:
            print("1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, "
                  "\nи проверяет, является ли этот день выходным.")
            if_holiday(enter_number("Enter the number of the day of the week from 1 to 7 \n> "))
        elif num == 2:
            print("2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n"
                  "для всех значений предикат.")
            check_predicate(enter_list())
        elif num == 3:
            quarter_number()
        elif num == 0:
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


def if_holiday(day_number):
    if int(day_number) == 6 or int(day_number) == 7:
        print(f'The entered day of the week is a holiday, Congratulations\n')
    else:
        print("The entered day of the week is NOT a holiday, sorry\n")


# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

def enter_list():
    result = [input('Enter x,y,z (3 numbers) separated by a space\n> ').split()]
    return result


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    print(result)


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
            print("X or Y can't be equal to 0, please try again.\n")
        else:
            break
    if x > 0 and y > 0:
        print(f'\nThe quarter number for\nx = {x}\ny = {y}\nis I quarter')
    elif x < 0 < y:
        print(f'\nThe quarter number for\nx = {x}\ny = {y}\nis II quarter')
    elif x < 0 and y < 0:
        print(f'\nThe quarter number for\nx = {x}\ny = {y}\nis III quarter')
    elif y < 0 < x:
        print(f'\nThe quarter number for\nx = {x}\ny = {y}\nis IV quarter')


lets_go()
