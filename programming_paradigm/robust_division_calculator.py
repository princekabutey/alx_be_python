def safe_divide(numerator, denominator):
    """
    Performs division with error handling for division by zero and non-numeric inputs.

    Args:
        numerator (str): Numerator value as a string.
        denominator (str): Denominator value as a string.

    Returns:
        str: Result of division or error message.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
