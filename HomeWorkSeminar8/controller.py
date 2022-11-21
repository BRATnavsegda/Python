import view_tk
import view_cli
import csv


def start(grafics):
    if grafics == 1:
        view_cli.start_cli()
    else:
        view_tk.init()


def write_in(file, input_data):  # записать в файл
    with open(file, 'w', encoding='utf-8', newline='') as data:
        writer = csv.writer(data)
        for row in input_data.items():
            writer.writerow(row)


def read_in(file):  # считать из файла
    res = {}
    with open(file, 'r', encoding='utf-8') as data:

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


def add_contact(fio, tel_number, catalog='numbers.csv'):
    cat = read_in(catalog)
    i = 1
    for key in cat:
        if int(key) == i:
            i += 1
    cat[i] = f'{fio} / {tel_number}'
    write_in('numbers.csv', cat)


def get_data_from_database(file='numbers.csv') -> list:
    res = []
    with open(file, 'r', encoding='utf-8') as data:
        res.extend(csv.reader(data))
    return res


def splitter(file) -> list:
    res_str = file[1].split('\\')
    res = [res_str[0]] + [res_str[1]]
    return res


def re_splitter(data):
    res: str = data[0] + '\\' + data[1]
    return res
