import random


print('1.Задайте последовательность чисел.\n'
      'Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.\n')

lst = list(random.randint(1, 10) for i in range(1, 20))
print(f"Исходный список: {lst}")

result = list(filter(lambda n: lst.count(n) == 1, lst))

print(f"Список из неповторяющихся элементов: {result}\n\n")


print('2.Задайте список из нескольких чисел. Напишите программу,\n'
      'которая найдёт сумму элементов списка, стоящих на нечётной позиции.')

lst = [random.randint(1, 10) for i in range(1, 8)]
print(f'\nЭто ваш список:\n{lst}')

res = 0
for i, k in enumerate(lst):
    res = res + k if i % 2 == 1 else res
print(f'\nСуммой элементов стоящих на нечётных позициях вашего списка будет: {res}\n\n')


print('3.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".')


text = "абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв"
print("<<<(введите строку для проверки либо нажмите Enter, если не хотите)>>>")
user_choice = input("-->")
if not user_choice:
    user_choice = text
    print("Тогда используем эту строку для проверки:\n"
          "абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв\n")

lst = ' '.join(list(filter(lambda s: 'абв' not in s, user_choice.split())))
print(f"Результат:\n{lst}\n")


print('4.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')

res: int = 0
num = round(float(random.uniform(0, 10)), 2)
print(f'\nСлучайное вещественное число в диапазоне 0-10 \n{num}')
lst_num = list(map(int, str(abs(num)).replace('.', '')))
# res = res+i for i in lst_num
for i in lst_num:
    res += i

print(f'Сумма цифр вашего числа > {int(res)} <')


