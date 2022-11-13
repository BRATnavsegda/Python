x = 1
y = 1


def init(a,b):
    global x
    global y
    x = int(a)
    y = int(b)

# summa = lambda x,y : x + y

def summa():
    return x + y

def prod():
    return x * y

def dif():
    return x - y

def div():
    return x / y

def pov():
    return x ** y

op_cod = "[ +  *  -  /  **]"

operations = {'+':summa, '*':prod, '-':dif, '/':div, '**':pov} 