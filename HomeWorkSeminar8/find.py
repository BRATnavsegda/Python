import csv
a = ['1', 'Шурик электрик \\ 8-999-234-34-20']

def splitter(file) -> list:
    res_str = file[1].split('\\')
    res = [[res_str[0]], [res_str[1]]]
    return res


splitter(a)