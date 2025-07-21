# Simple Python program that greets the user and adds two numbers

# Ask for the user's name
name = input("What is your name? ")

# Greet the user
print(f"Hello, {name}! Let's do some simple math.")

# Ask for two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2

    # Show the result
    print(f"The sum of {num1} and {num2} is {total}.")

except ValueError:
    print("Please enter valid numbers.")
