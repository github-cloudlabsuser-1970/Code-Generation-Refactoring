# Create a basic calculator that can do the following operations:
# Add, Subtract, Multiply, Divide, Power, Square Root, Factorial

# Importing the math module
import math as m

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Square root of a negative number is not allowed."
    return m.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial of a negative number is not defined."
    return m.factorial(a)

# Example usage with user input
if __name__ == "__main__":
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))

        elif choice == '6':
            num = float(input("Enter a number: "))
            print("Result:", square_root(num))

        elif choice == '7':
            num = int(input("Enter a number: "))
            print("Result:", factorial(num))

        else:
            print("Invalid input. Please try again.")