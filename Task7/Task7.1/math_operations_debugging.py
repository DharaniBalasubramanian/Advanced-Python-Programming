# math_operations.py (Bug fixes applied) using print(statements)

def add(a, b):
    print(f"Debugging add: a={a}, b={b}")
    result = a + b  # Remove str() to return the result as a number
    print(f"Result of add: {result}")
    return result


def subtract(a, b):
    print(f"Debugging subtract: a={a}, b={b}")
    result = a - b  # Correct the order of subtraction
    print(f"Result of subtract: {result}")
    return result


def multiply(a, b):
    print(f"Debugging multiply: a={a} (type={type(a)}), b={b} (type={type(b)})")
    result = a * b  # Perform actual multiplication, not string repetition
    print(f"Result of multiply: {result}")
    return result


def divide(a, b):
    print(f"Debugging divide: a={a}, b={b}")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")  # Raise the error instead of returning 0
    result = a / b
    print(f"Result of divide: {result}")
    return result


