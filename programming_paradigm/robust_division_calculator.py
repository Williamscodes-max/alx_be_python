def safe_divide(numerator, denominator):
    """
    Attempts to divide numerator by denominator.
    Returns a message string for errors or the result message on success.
    """
    # Check numeric conversion
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Check division by zero and perform division
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
