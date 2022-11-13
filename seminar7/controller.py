import model
import view
import test_input as ti

def start():

    view.showinfo("hello! welcome to calculator!")
    while True:
        a = view.getNumb("input int value --> ")
        if not ti.test_int(a):
            view.showinfo("not correct input")
            continue
        b = view.getNumb("input int value --> ")
        if not ti.test_int(b):
            view.showinfo("not correct input")
            continue

        op = view.getNumb(f"input operation {model.op_cod}")

        if ti.test_int(a) and ti.test_int(b) and ti.test_operations(op, model.operations.keys()):
            break
        else:
            view.showinfo("not correct input")

    model.init(a,b)

    result = model.operations[op]()

    view.showinfo(result)