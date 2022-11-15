import csv


def write_in(file, input_data):  # записать в файл
    with open(file, 'w', newline='') as data:
        writer = csv.writer(data)
        for row in input_data.items():
            writer.writerow(row)


def read_in(file):  # считать из файла
    res = {}
    with open(file, 'r') as data:

        for count, name_number in csv.reader(data):
            res[count] = name_number
        return res


def add_in(file, input_data):  # добавить строку в файл
    f = open(file, 'r')
    s = f.read()
    f.close()
    l = s.splitlines()
    l.insert(0, str(input_data))
    s = '\n'.join(l)
    f = open(file, 'w')
    f.write(s)
    f.close()


def dict_from_files():  # собрать построчно из 2 файлов в 1 словарь
    fio_file = read_in('FIO.txt')
    nums_file = read_in('numbers.csv')
    result = dict(zip(fio_file, nums_file))
    return result


