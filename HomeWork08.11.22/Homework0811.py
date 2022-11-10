import random


# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(random.randint(1, 10) for i in range(1, 20))
print(f"Исходный список: {lst}")

result = list(filter(lambda n: lst.count(n) == 1, lst))

print(f"Список из неповторяющихся элементов: {result}\n\n")


# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [random.randint(1, 10) for i in range(1, 8)]
print(f'\nЭто ваш список:\n{lst}')

res = 0
for i, k in enumerate(lst):
    res = res + k if i % 2 == 1 else res
print(f'\nСуммой элементов стоящих на нечётных позициях вашего списка будет: {res}')

