import os
def screen_cleaner():
    if os.name =='nt':
        os.system("cls")
    else:
        os.system("clear")

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

arithmetic_signs = {
    "+" : add,
     "-" : subtract,
     "*" : multiply,
     "/" : division
}

def calculator():
    To_continue = True
    number1= float(input("what is your first number?: "))
    while To_continue:
        for symbols in arithmetic_signs:
            print(symbols)
        operation = input("Pick an operation: ")
        number2=float(input("Whats the next number: "))
        result=arithmetic_signs[operation](number1,number2)
        print(f"{number1} {operation} {number2} = {result}")

        calculate_again=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if calculate_again == 'y':
            number1 = result
        else:
            To_continue = False
            screen_cleaner()
            break
calculator()
