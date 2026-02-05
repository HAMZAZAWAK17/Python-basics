#Les conditions:
#exemple 1:
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

operation = input("enter operation (+, -, *, /)")

if operation == "+":
    print("result:", num1 + num2)
elif operation == "-":
    print("result:", num1 - num2)
elif operation == "*":
    print("result:", num1 * num2)
elif operation == "/":
    print("result:", num1 / num2)
else:
    print("invalid operation")
