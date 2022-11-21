from tkinter import filedialog, ttk
from tkinter import *
import controller


main_window = None
main_table = None


# def start_tk():



def init():
    global main_window

    main_window = Tk()

    init_main_window()
    init_control_panel()
    init_main_table()
    fill_main_table()
    main_window.mainloop()


def init_main_window():
    w = main_window.winfo_screenwidth()
    h = main_window.winfo_screenheight()
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 200  # смещение от середины
    h = h - 200

    main_window.title('Телефонный справочник')
    main_window.geometry((f'700x400+{w}+{h}'))


def init_main_table():
    global main_table

    main_table = ttk.Treeview(main_window, show='headings', columns=['Наименование', 'Телефон'], name='table_main')
    main_table.column('Наименование', width=200, anchor=W)
    main_table.column('Телефон', width=100, anchor=E)
    main_table.heading('Наименование', text='Наименование', anchor=CENTER)
    main_table.heading('Телефон', text='Телефон', anchor=CENTER)

    # for i in range(10):
    #     main_table.insert('',i,values=(1,2))

    main_table.pack(expand=1, side=TOP, fill=BOTH)


def init_control_panel():
    top_panel = ttk.Frame(main_window, name='top_panel')
    top_panel.pack(side=TOP, fill=BOTH)

    field_find = ttk.Entry(top_panel, width=50, name='entry_find')
    field_find.pack(side=LEFT, padx=5, pady=5)

    btn_find = ttk.Button(top_panel, text='Найти', command=btn_find_click)
    btn_find.pack(side=LEFT, pady=5)

    btn_remove = ttk.Button(top_panel, text='Удалить', command=btn_remove_click)
    btn_remove.pack(side=LEFT, padx=10, pady=5)

    # btn_load = ttk.Button(top_panel, text='Добавить', command=btn_add_click())
    # btn_load.pack(side=LEFT, pady=5)


def fill_main_table(str_pattern=''):
    global main_table
    i = 0
    data = controller.get_data_from_database()
    del data[0]
    for elem in data:
        a = controller.splitter(elem)
        main_table.insert('', i, values=a)
        i += 1



def btn_find_click():
    str_query = main_window.children['top_panel'].children['entry_find'].get()
    if str_query == '':
        clean_main_table()
        fill_main_table()
    else:
        cat = controller.read_in('numbers.csv')
        print(cat)
        key = ''
        for k, v in cat.items():
            if str_query in v:
                key = k


        clean_main_table()
        fill_main_table(key)  # продолжить заполнение только одного поля


def btn_add_click():
    str_query = main_window.children['top_panel'].children['entry_find'].get()
    res = str_query.split('/')
    fio, tel_number = res[0], res[1]
    controller.add_contact(fio, tel_number)
    clean_main_table()
    fill_main_table()


def btn_remove_click():
    data = tuple(main_table.item(main_table.focus())['values'])
    cat = controller.read_in('numbers.csv')
    if data == ():
        return
    data_str = controller.re_splitter(data)
    temp = ''
    for k, v in cat.items():
        if v == data_str:
            temp = k
            print(k)
    del cat[temp]

    print(cat)
    i = 0
    for key in cat.copy():
        if int(key) == i:
            i += 1
        else:
            cat[i] = cat[key]
            del cat[key]
            i += 1
    controller.write_in('numbers.csv', cat)
    clean_main_table()
    fill_main_table()


def clean_main_table():
    for i in main_table.get_children():
        main_table.delete(i)

# from tkinter import *
# from tkinter import ttk
#

# root = None
# frm = None
#
#
# def create_menu():
#     global root
#     global frm
#     root = Tk()
#     frm = ttk.Frame(root, padding=100)
#     frm.grid()
#     ttk.Button(frm, text="Дни до нового года", command=print_result).grid(column=0, row=1)
#     ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
#     root.mainloop()
#
#
# def show_info(text):
#     global frm
#     ttk.Label(frm, text=f'{text}').grid(column=1, row=1)
