 # prompt for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))

 # display operatin choice
print("Available operation")
print("+ : Addition")
print("- : substraction")
print("* : Multiplication")
print("/ : Division")

operation = input("Choose the operation (+, -, *, /):")

#perform calculation using Match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
            if num2 != 0:
                 result = num1 / num2
                 print(f"The result is {result}.")
            else:
                 print("Cannot divide by zero.")

