def calculator():
    print("simple calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# prompt for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+, -, *, /):")

match operator:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1- num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
           resut = num1 / num2
           print(f"The result is {resut}.")
        else:
             print("cannot divide by zero")

    
     
        
        
    

    

   
    