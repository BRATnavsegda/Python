def lets_go():
    while True:
        print("\n<<<Enter the task number from 1 to 5 to check.>>>\n"
              "\nFor quit enter 0")
        num = enter_number("> ")
        if int(num) == 1:
            print("1. Напишите программу, которая принимает на вход вещественное число "
                  "\nи показывает сумму его цифр.")
            count_numbers()
        elif int(num) == 2:
            print("2. Напишите программу, которая принимает на вход число N \n"
                  "и выдает набор произведений чисел от 1 до N.")
            factorial_n()
        elif int(num) == 3:
            print("3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.")
            for_task3()
        elif int(num) == 4:
            print(" 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].\n"
                  "Найдите произведение элементов на указанных позициях.\n"
                  "Позиции вводятся с клавиатуры.")
            for_task4()
        elif int(num) == 5:
            print("5. Реализуйте алгоритм перемешивания списка.")

        elif int(num) == 0:
            print("\nАнекдот напоследок: \n\n"
                  "Instagram был заблокирован в России.\n"
                  "Количество пользователей из Нидерландов увеличилось на 59 млн.\n")
            break
        else:
            print("Enter the correct number, please")


def enter_number(message):
    number = input(message)
    try:
        float(number)

    except ValueError:
        print("Please enter the number, try again!")
        return enter_number(message)
    return number


# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11

def count_numbers():
    result = 0
    num = abs(int(enter_number("Enter the number\n>").replace('.', '')))
    while num > 0:
        digit = num % 10
        result = result + digit
        num = num // 10
    print(f'The sum of the digits of your number is > {int(result)} <')


# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial_n():
    result: int = 1
    res_list = []
    n = abs(int(enter_number("Enter positive number:\nN = ")))
    for i in range(n):
        if i <= n:
            i += 1
            result *= i
            res_list.append(result)
    print(res_list)


# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#
# *Пример:*
#
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06


def for_task3():
    num = int(enter_number("Enter your number\nn = "))
    result = {}
    for i in range(num):
        i += 1
        result[i] = round(((1 + 1 / i) ** i), 2)
    print(result)


# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


def for_task4():
    num = int(enter_number("Enter the number to create the list:\n N = "))
    n_list = []
    temp = -num - 1

    while num != temp:
        temp += 1
        n_list.append(temp)
    print(f"This is your list:\n{n_list}")

    first_num = int(enter_number("Enter number one for product of elements:\n №1 = "))
    second_num = int(enter_number("Enter number two for product of elements:\n №2 = "))

    if 0 < first_num <= len(n_list) and 0 < second_num <= len(n_list):
        result = n_list[first_num-1] * n_list[second_num-1]
        print(f"The product of elements at specified positions: {result}")
    else:
        print("No such list item, please try again")
        return for_task4()




# 5) Реализуйте алгоритм перемешивания списка.


lets_go()
