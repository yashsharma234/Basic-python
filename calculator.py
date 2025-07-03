#  calculator by using basics of python programming

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operator!"

print("Welcome to CodSoft's Calculator 🚀")
print("Available operations: +  -  *  /")

# Get input from user
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Show result
result = calculate(num1, operator, num2)
print("Result:", result)