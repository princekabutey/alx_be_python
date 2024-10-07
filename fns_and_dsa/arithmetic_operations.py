def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Performs basic arithmetic operations.

    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): Arithmetic operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: Result of the operation or error message.
    """

    from arithmetic_operations import perform_operation   

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
result = perform_operation(num1, num2, operation)

print(f"Result: {result}")





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   