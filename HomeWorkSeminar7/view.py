# from tkinter import *
# from tkinter import ttk
#
#
# root = None
# frm = None
#
# def createMenu():
#     global root
#     global frm
#     root = Tk()
#     frm = ttk.Frame(root, padding=100)
#     frm.grid()
#     ttk.Button(frm, text="Дни до нового года", command=print_result).grid(column=0, row=1)
#     ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
#     root.mainloop()
#
# def showinfo(text):
#     global frm
#     ttk.Label(frm, text=f'{text}').grid(column=1, row=1)

def showinfo(a):
    print(a)

def getValue(b):
    return input(b)

