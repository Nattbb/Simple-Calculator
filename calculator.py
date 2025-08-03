def simple_calc():
    # Get user inputs
    num1_str = input("Enter the first number: ")
    op = input("Enter operation (+, -, *, /): ").strip()
    num2_str = input("Enter the second number: ")

    # Try converting inputs to float
    try:
        a = float(num1_str)
        b = float(num2_str)
    except ValueError:
        print("Error: One or both inputs are not valid numbers.")
        return

    # Perform the operation
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            print("Error: Division by zero.")
            return
        result = a / b
    else:
        print("Error: Operation not recognized. Please enter one of +, -, *, /.")
        return

    # Display the result
    print(f"{a} {op} {b} = {result}")


if __name__ == "__main__":
    simple_calc()
