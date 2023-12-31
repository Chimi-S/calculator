from art import logo
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's your first number: "))
    for operation in operations:
        print(operation)

    continue_calculation = True

    while continue_calculation:

        operation_choice = input("Pick an operation from the line above: ")
        num2 = float(input("What's your second number: "))

        calculation_function = operations[operation_choice]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_choice} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            continue_calculation = False
            clear()
            calculator()


calculator()
