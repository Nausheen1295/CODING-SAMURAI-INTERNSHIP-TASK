def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def calculator():
    print("Welcome to the Advanced Command-Line Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. View History")
    print("8. Exit")

    history = []

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"
            elif choice == '5':
                result = exponentiate(num1, num2)
                operation = f"{num1} ** {num2} = {result}"
            elif choice == '6':
                result = modulus(num1, num2)
                operation = f"{num1} % {num2} = {result}"

            print(operation)
            history.append(operation)

        elif choice == '7':
            print("\nCalculation History:")
            if history:
                for entry in history:
                    print(entry)
            else:
                print("No calculations have been performed yet.")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
