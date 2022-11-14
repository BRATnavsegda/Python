# import model
import view
import files_work as fw


def start():
    view.showinfo("\n\nПривет! Это плохой телефонный справочник!\n")
    while True:

        view.showinfo("\nВы хотите считать сохраненные номера или добавить новый?\n\n"
                      "\tВвести новый номер, введите цифру 1\n"
                      "\tСчитать записанные номера, введите цифру 2\n"
                      "\n\n\t>>>Для выхода введите что угодно, кроме указанного выше<<<\n")
        action = int(view.getValue('--> '))

        if action == 1:
            fio = view.getValue('Введите ФИО: ')
            tel_number = view.getValue('Введите номер ')
            fw.add_in('numbers.txt', tel_number)
            fw.add_in('FIO.txt', fio)
        elif action == 2:
            print()
            phone_book = fw.dict_from_files()
            for i, j in phone_book.items():
                print(f'{i} - {j}')
        else:
            break


    # model.init(fio, tel_number)



