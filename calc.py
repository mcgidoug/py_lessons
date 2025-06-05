def calculator():
    print("Welcome to the Python Calculator!")

    # Get the first number from the user
    num1 = float(input("Enter the first number: "))

    # Get the operation (+, -, *, /)
    operation = input("Choose an operation (+, -, *, /): ")

    # Get the second number from the user
    num2 = float(input("Enter the second number: "))

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Oops! Can't divide by zero."
    else:
        result = "Invalid operation!"

    print("The result is:", result)

# Call the function to run the calculator
calculator()

