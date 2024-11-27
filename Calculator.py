# Calculator
# 11/27/2024

def Calculation(operator):
    firstNumber = int(input("Enter a first number: "))
    secondNumber = int(input("Enter a second number: "))

    if operator == "+":
        Result = firstNumber + secondNumber
    elif operator == "-":
        Result = firstNumber - secondNumber
    elif operator == "*":
        Result = firstNumber * secondNumber
    elif operator == "/":
        Result = firstNumber / secondNumber

    print(firstNumber, operator, secondNumber, "=", Result)

calculationSelection = input("Select a operator to calculate with (+ - * /): ")

if calculationSelection in ["+", "-", "*", "/"]:
    Calculation(operator=calculationSelection)
else:
    print("It isn't an operator")