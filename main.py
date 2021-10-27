from art import logo
import os


def clear(): return os.system('clear')


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": devide,
}


def calculator():
    print(logo)

    continue_calculating = True
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    while continue_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(
            f"'y' to continue calculating with {answer}, 'n' to start new calculation: ")
        if should_continue == "n":
            continue_calculating = False
            clear()
            calculator()
        else:
            num1 = answer


calculator()
