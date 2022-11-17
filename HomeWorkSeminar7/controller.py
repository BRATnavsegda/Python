import csv_to_json
import view
import files_work as fw


def start():
    view.showinfo("\n\nПривет! Это плохой телефонный справочник!\n")
    while True:

        view.showinfo("\nВы хотите считать сохраненные номера или добавить новый?\n\n"
                      "\tВвести новый номер, введите цифру 1\n"
                      "\tПосмотреть записанные номера, введите цифру 2\n"
                      "\tУдалить один из номеров, введите цифру 3\n"
                      "\n\n\t>>>Для выхода введите что угодно, кроме указанного выше<<<\n")
        action = int(view.getValue('--> '))

        if action == 1:
            cat = fw.read_in('numbers.csv')
            fio = view.getValue('Введите наименование: ')
            tel_number = view.getValue('Введите телефонный номер ')
            i = 1
            for key in cat:
                if int(key) == i:
                    i += 1
            cat[i] = f'{fio} / {tel_number}'
            fw.write_in('numbers.csv', cat)

        elif action == 2:
            print()
            cat = fw.read_in('numbers.csv')
            view.showinfo('Уже сохраненные контакты:\n')
            for i, j in cat.items():
                view.showinfo(f'{i}, {j}')
        elif action == 3:
            print()
            cat = fw.read_in('numbers.csv')
            view.showinfo('Уже сохраненные контакты:\n')
            for i, j in cat.items():
                view.showinfo(f'{i}, {j}')
            del_num = view.getValue('Введите порядковый номер контакта для удаления\n-->')

            if cat[del_num]:
                del cat[del_num]

            i = 0
            for key in cat:
                if int(key) == i:
                    i += 1
                else:
                    cat[i] = cat[key]
                    del cat[key]
                    i += 1
            fw.write_in('numbers.csv', cat)
        else:
            view.showinfo('Ваша телефонная книга сохранена в 2 форматах: csv и json.')
            csv_to_json.make_json()
            break
