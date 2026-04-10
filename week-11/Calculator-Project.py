from art import logo

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

    first_number = float(input("What's the first number?: "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_number, next_number)

        print(f"{first_number} {operation_symbol} {next_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()