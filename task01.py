def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 0
    return a / b

def calculate(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return 0

operator = input("operatorni kriting: ")
num1 = float(input("a qiymatni kiriting: "))
num2 = float(input("b qiymatni kirting: "))
print(calculate(num1, num2, operator))