def calculator(number1, number2, operation):
    if operation == "+":
        print(number1 + number2)
    if operation == "-":
        print(number1 - number2)
    if operation == "*":
        print(number1 * number2)
    if operation == "/":
        print(number1 / number2)


print("Enter Number 1:")
a = int(input())
print("Enter Number 2 :")
b = int(input())
print("What you want to do ?")
c = str(input())
print("This is what you got: ")
calculator(a, b, c)
