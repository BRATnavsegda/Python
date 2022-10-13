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

        elif int(num) == 3:
            print("3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.")

        elif int(num) == 4:
            print(" 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].\n"
                  "Найдите произведение элементов на указанных позициях.\n"
                  "Позиции вводятся с клавиатуры.")

        elif int(num) == 5:
            print("5. Реализуйте алгоритм перемешивания списка.")

        elif int(num) == 0:
            print("\nАнекдот напоследок: \n\n"
                  "Подскажите, а печатать дома на цветном принтере доллары\n"
                  "и евро — это еще статья за фальшивомонетничество или уже медаль за импортозамещение?")
            break
        else:
            print("Enter the correct number, please")


def enter_number(message):
    number = input(message)
    try:
        float(number)

    except ValueError:
        print("Please enter the number, try again!")
        number = 0
        enter_number(message)
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
    n = enter_number("Enter number:\nN = ")
    for i in range(n):
        if i <= n:
            i += 1
            result *= i
            print(result)


# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#
# *Пример:*
#
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06


# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


# 5) Реализуйте алгоритм перемешивания списка.


lets_go()
