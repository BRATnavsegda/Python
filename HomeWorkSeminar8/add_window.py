from tkinter import *
from tkinter import ttk
import controller as ctrl

window = None
feet_fio = None
feet_tel_number = None
feet_job_title = None
feet_age = None
feet_salary = None


def calculate():
    global window
    data = (feet_fio.get() + ' / ' + feet_tel_number.get() + ' / ' + \
            feet_job_title.get() + ' / ' + feet_age.get() + ' / ' + feet_salary.get()).replace(',', '.')
    # a = feet_job_title.get()
    # print(type(a), a)
    ctrl.add_contact_all(data)
    window.destroy()


def get_value():
    global window
    global feet_fio
    global feet_tel_number
    global feet_job_title
    global feet_age
    global feet_salary

    window = Tk()
    window.title("Добавление нового служащего")

    mainframe = ttk.Frame(window, padding="100 50 50 50")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    style = ttk.Style()  # подключаем модуль стилей
    style.configure("BW.TLabel", foreground="white", background="black")  # создаем шаблон стиля

    feet_fio = StringVar()
    feet_fio_entry = ttk.Entry(mainframe, width=50, textvariable=feet_fio)
    feet_fio_entry.grid(column=2, row=1, sticky=(W, E))
    ttk.Label(mainframe, text='Введите ФИО служащего:').grid(column=1, row=1, sticky=W)

    feet_tel_number = StringVar()
    feet_tel_number_entry = ttk.Entry(mainframe, width=50, textvariable=feet_tel_number)
    feet_tel_number_entry.grid(column=2, row=2, sticky=(W, E))
    ttk.Label(mainframe, text='Введите телефонный номер служащего:').grid(column=1, row=2, sticky=W)

    feet_job_title = StringVar()
    feet_job_title_entry = ttk.Entry(mainframe, width=50, textvariable=feet_job_title)
    feet_job_title_entry.grid(column=2, row=3, sticky=(W, E))
    ttk.Label(mainframe, text='Укажите должность служащего:').grid(column=1, row=3, sticky=W)

    feet_age = StringVar()
    feet_age_entry = ttk.Entry(mainframe, width=50, textvariable=feet_age)
    feet_age_entry.grid(column=2, row=4, sticky=(W, E))
    ttk.Label(mainframe, text='Укажите возраст служащего:').grid(column=1, row=4, sticky=W)

    feet_salary = StringVar()
    feet_salary_entry = ttk.Entry(mainframe, width=50, textvariable=feet_salary)
    feet_salary_entry.grid(column=2, row=5, sticky=(W, E))
    ttk.Label(mainframe, text='Укажите оклад служащего:').grid(column=1, row=5, sticky=W)

    ttk.Label(mainframe, text='Введите данные, нажмите кнопку добавить и закройте окно',
              style="BW.TLabel").grid(column=2, row=6, sticky=W)

    ttk.Button(mainframe, text="Добавить", command=calculate).grid(column=2, row=7, sticky=N)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    feet_fio_entry.focus()  # первоначальное расположение курсора ввода

    window.bind("<Return>", calculate)

    window.mainloop()



# get_value('text')
# print(data)

