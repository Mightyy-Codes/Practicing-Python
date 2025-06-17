history = []
def calculator():  # Simple calculator function
    try: # Try-except block to handle exceptions
        num1 = float(input("Enter the first number: "))
        print("Available operators: +, -, *, /, %, **")
        operator = input("Enter an operator: ")
        num2 = float(input("Enter the second number: "))
        print("Available operators: +, -, *, /, %, **")
        operator = input("Enter an operator: ")
        num3 = float(input("Enter the third number: "))

        if operator == "+":
            result = num1 + num2 + num3
        elif operator == "-":
            result = num1 - num2 - num3
        elif operator == "*":
            result = num1 * num2 * num3
        elif operator == "/":
            if num2 == 0:
                result = "Error: Cannot divide by zero."
            else:
                result = num1 / num2 / num3
        elif operator == "%":
            result = num1 % num2 % num3
        elif operator == "**":
            result = num1 ** num2 ** num3
        else:
            result = "Invalid operator."
        
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    if isinstance(result, float): # Check if result is a float
        result = round(result, 2)
        if result.is_integer(): # Check if result is an integer
            result = int(result)
        history.append(f"{num1} {operator} {num2} = {result}")

while True: # Loop to allow multiple calculations
     calculator()
     again = input ("Do you want to calculate again? (yes/no/history): ")
     if again.lower() == "history": # Check if user wants to see history
        print("\n Calculation History:")
        for entry in history:
            print(entry)
     if again.strip() == "": # Check for empty input & continues when enter is pressed
        continue
     if again.strip().lower() != "yes": # Check if user wants to exit
        print("Thanks for using the calculator!")
        break