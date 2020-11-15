def add(x, y):
    res = x + y
    return res

def subtract(x, y):
    res = x - y
    return res

def multiply(x, y):
    res = x * y
    return res

def divide(x, y):
    res = x / y
    return res

def operation(oper, num1, num2):
    if oper == '+':
        res = add(first_num, sec_num)
        return res
    elif oper == '-':
        res = subtract(first_num, sec_num)
        return res
    elif oper == '*':
        res = multiply(first_num, sec_num)
        return res
    elif oper == '/':
        res = divide(first_num, sec_num)
        return res

while True:
    first_num = int(input("Whats the first number?:\n"))
    print("+ - * /")
    oper = input("What operation would you like to perform?\n")
    sec_num = int(input("Whats the second number?\n"))

    res = operation(oper, first_num, sec_num)

    while True:
        con_oper = input(f"Type 'y' to continue calculation with {res}, or type 'n' to start a new calculation:\n").lower()
        if con_oper == 'y':
            print("+ - * /")
            first_num = res
            oper = input("What operation would you like to perform?\n")
            sec_num = input("Whats the second number?\n")
            res = int(operation(oper, res, sec_num))
        else:
            break

    break
