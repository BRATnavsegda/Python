import controller
import csv_to_json


def show_info(a):
    print(a)


def get_value(b):
    return input(b)


def start_cli():
    show_info("\n\nПривет! Это информационная система какой-то компании!\n")
    while True:

        show_info("\nВы хотите считать сохраненные контакты или добавить новый?\n\n"
                  "\tДобавить нового служащего, введите цифру 1\n"
                  "\tПосмотреть записанные контакты, введите цифру 2\n"
                  "\tУдалить один из контактов, введите цифру 3\n"
                  "\n\n\t>>>Для выхода введите что угодно, кроме указанного выше<<<\n")
        action = int(get_value('--> '))

        if action == 1:
            fio = get_value('Введите ФИО служащего: ')
            tel_number = get_value('Введите телефонный номер служащего: ')
            job_title = get_value('Укажите должность служащего: ')
            age = get_value('Укажите возраст служащего: ')
            salary = get_value('Укажите оклад служащего: ').replace(',', '.')
            controller.add_contact(fio, tel_number, job_title, age, salary)

        elif action == 2:
            print()
            cat = controller.read_in('numbers.csv')
            show_info('Уже сохраненные контакты:\n')
            for i, j in cat.items():
                show_info(f'{i}, {j}')
        elif action == 3:
            print()
            cat = controller.read_in('numbers.csv')
            show_info('Уже сохраненные контакты:\n')
            for i, j in cat.items():
                show_info(f'{i}, {j}')
            del_num = get_value('Введите порядковый номер контакта для удаления\n-->')

            if cat[del_num]:
                del cat[del_num]

            i = 0
            for key in cat.copy():
                if int(key) == i:
                    i += 1
                else:
                    cat[i] = cat[key]
                    del cat[key]
                    i += 1
            controller.write_in('numbers.csv', cat)
        else:
            show_info('Ваша информационная система сохранена в 2 форматах: csv и json.')
            csv_to_json.make_json()
            break
