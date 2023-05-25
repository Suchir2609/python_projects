# This is a sample Python script.


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operator = {
    '+' : add,
    '-': subtract,
    '*' : multiply,
    '/' : divide,
}
def calculator():
    """executes the calculator"""
    num1 = float(input("what is the first number? :"))
    continue_input = True
    while continue_input:
        num2 = float(input("what is the next number? :"))
        for key in operator:
            print(key)
        operator_input = input("chose an operator: ")
        calc_funcion = operator[operator_input]
        answer = calc_funcion(num1,num2)
        print(f"{num1}{operator_input}{num2} = {answer}")
        choice = input(f"enter 'y' to continue with {answer} an first number, or enter 'n' to exit: ")
        if choice == "y":
            continue_input = True
            num1 = answer
        else:
            continue_input = False
            calculator()

calculator()