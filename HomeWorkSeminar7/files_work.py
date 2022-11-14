
def write_in(file, input_data):  # записать в файл
    with open(file, 'w') as data:
        data.write(input_data)


def read_in(file):  # считать из файла
    with open(file, 'r') as data:
        r = data.read().splitlines()
        return r


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


def dict_from_files():
    fio_file = read_in('FIO.txt')
    nums_file = read_in('numbers.txt')
    result = dict(zip(fio_file, nums_file))
    return result


