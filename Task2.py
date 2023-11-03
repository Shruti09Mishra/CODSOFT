# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Main function to get user input and perform calculations
def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter operation choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            operation = "Addition"
        elif choice == 2:
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == 3:
            result = multiply(num1, num2)
            operation = "Multiplication"
        else:
            result = divide(num1, num2)
            operation = "Division"

        print(f"{operation} result: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
