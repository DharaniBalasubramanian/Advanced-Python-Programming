def add(a, b):
    return str(a + b)  # Bug 1: Returning result as string instead of number

def subtract(a, b):
    return b - a  # Bug 2: Reversed order of subtraction

def multiply(a, b):
    return str(a) * b  # Bug 3: Converting a to string and multiplying (string repetition instead of actual multiplication)

def divide(a, b):
    if b == 0:
        return 0  # Bug 4: Returning 0 instead of raising ZeroDivisionError
    return a / b


print("Addition:", add(3, 6))         
print("Subtraction:", subtract(10, 4))
print("Multiplication:", multiply(4, 5)) 
print("Division:", divide(15, 0))    
