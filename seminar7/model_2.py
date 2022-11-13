x = 1
y = 1


def init(a,b):
    global x
    global y
    x = int(a)
    y = int(b)


def summa():
    return x + y

def prod():
    return x * y

def dif():
    return x - y

def div():
    return x / y

op_cod = "[ +  *  -  / ]"

operations = {'+':summa, '*':prod, '-':dif, '/':div}