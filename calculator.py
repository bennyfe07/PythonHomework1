number1 = int(input("Please type in a number: "))
number2 = int(input("Please type in a second number: "))

operation = input("Choose an arithmetic operation (+,-,*,/): ")

if operation == "+":
    print(number1 + number2)

elif operation == "-":
    print(number1 - number2)

elif operation == "*":
    print(number1 * number2)

elif operation == "/":
    print(number1 / number2)

else:
    print("You didn't type in an arithmetic operation.")
