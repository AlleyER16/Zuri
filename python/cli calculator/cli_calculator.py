print("CLI Calculator")
print("\nYou input should be in format [operand1 operator operand2]")
print("e.g 2 + 2, 4 * 5, 3 / 3, 10 - 5, 4 % 3")

print("\nAllowed Operators")
print("+ for addition")
print("- for substraction")
print("* for multiplication")
print("/ for division")
print("% for modulus")

print()

user_input = input("Enter expression: ")

expression = user_input.split(" ")

if len(expression) == 3:
    try:
        operand1 = int(expression[0])
        operator = expression[1]
        operand2 = int(expression[2])

        if operator in "+*/-%":
            if operator == "+":
                print(f"{user_input} = {operand1 + operand2}")
            elif operator == "-":
                print(f"{user_input} = {operand1 - operand2}")
            elif operator == "/":
                print(f"{user_input} = {operand1 / operand2}")
            elif operator == "*":
                print(f"{user_input} = {operand1 * operand2}")
            elif operator == "%":
                print(f"{user_input} = {operand1 % operand2}")
        else:
            print("Invalid operator")
    except:
        print("At least one of your operands is not a valid integer")
else:
    print("Invalid input format")