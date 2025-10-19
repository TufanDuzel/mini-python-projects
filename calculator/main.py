print("Calculator")

x = float(input("Please enter the first value: "))
y = float(input("Please enter the second value: "))

operation = ""

while operation not in ["+", "-", "*", "/"]:
    operation = input("(+, -, *, /) \nPlease select the operation: ")

    if operation == "+":
        print(x + y)
    elif operation == "-":
        print(x - y)
    elif operation == "*":
        print(x * y)
    elif operation == "/":
        print(x / y)
    else:
        print("Error: Please select an math operation.")