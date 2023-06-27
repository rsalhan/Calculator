num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operation = input("Enter 'x', '+', '-' or '/': ")

if operation == "+":
    result = num1 + num2
    print(num1, operation, num2)
    print("= " + str(result))
elif operation == "-":
    result = num1 - num2
    print(num1, operation, num2)
    print("= " + str(result))
elif operation == "x":
    result = num1 * num2
    print(num1, operation, num2)
    print("= " + str(result))
elif operation == "/":
    result = num1 / num2
    print(num1, operation, num2)
    print("= " + str(result))