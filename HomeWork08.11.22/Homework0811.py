import random


# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(random.randint(1, 10) for i in range(1, 20))
print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]

result = list(filter(lambda n: lst.count(n) == 1, lst))

print(f"Список из неповторяющихся элементов: {result}")


