from art import logo

# Math operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

# Operations dictionary
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
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation!")
            continue

        next_number = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_number, next_number)

        print(f"{first_number} {operation_symbol} {next_number} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ).lower()

        if choice == "y":
            first_number = answer
        elif choice == "n":
            print("\n" * 20)
            calculator()
            return
        else:
            print("Invalid input, exiting.")
            should_continue = False


calculator()