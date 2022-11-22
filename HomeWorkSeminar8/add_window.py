from tkinter import *
from tkinter import ttk

data = None
feet = None

def dismiss(window):
    calculate()
    window.destroy()

def calculate():
    global data
    global feet
    data = feet.get()


def get_value(text):
    global data
    global feet
    window = Tk()
    window.title("Добавление нового служащего")

    mainframe = ttk.Frame(window, padding="100 50 50 50")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    style = ttk.Style()  # подключаем модуль стилей
    style.configure("BW.TLabel", foreground="white", background="black")  # создаем шаблон стиля

    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=50, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    ttk.Button(mainframe, text="Добавить", command=lambda: dismiss(window)).grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text=text).grid(column=1, row=1, sticky=W)

    ttk.Label(mainframe, text='Введите данные, нажмите кнопку добавить и закройте окно',
              style="BW.TLabel").grid(column=2, row=2, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    feet_entry.focus()
    window.bind("<Return>", calculate)

    window.mainloop()

    return data

get_value('text')
print(data)



