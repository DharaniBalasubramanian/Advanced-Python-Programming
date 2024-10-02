def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference (a - b)."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the result of dividing a by b. Raises an error if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

print("Addition:", add(3, 6))         
print("Subtraction:", subtract(10, 4)) 
print("Multiplication:", multiply(4, 5)) 
print("Division:", divide(15, 3))     
