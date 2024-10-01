import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):  # zero division error
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not possible."

    # Exception handling for invalid inputs, overflow errors
    def safe_operation(self, operation, a, b=None):
        try:
            if b is not None:
                return operation(a, b)
            return operation(a)
        except (TypeError, OverflowError) as e:
            return f"Error: {e}"

    # Advanced math operations
    def square_root(self, a):
        if a < 0:
            return "Error: Square root of a negative number is invalid."
        return math.sqrt(a)

    def exponent(self, a, b):
        return self.safe_operation(math.pow, a, b)

    def logarithm(self, a, base=10):
        if a <= 0:
            return "Error: Logarithm of non-positive numbers is invalid."
        return math.log(a, base)


# Working of the calculator
calc = Calculator()

# Basic operations
print("Addition:", calc.add(2, 3))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(4, 3))
print("Division:", calc.divide(20, 5))
print("Division with denominator as Zero:", calc.divide(20, 0))

# Advanced operations
print("Square root:", calc.square_root(16))
print("Square root of -1:", calc.square_root(-1))
print("Exponentiation:", calc.exponent(2, 3))
print("Logarithm:", calc.logarithm(100, 10))
print("Logarithm of 0:", calc.logarithm(0))


def test_calculator():  # Testing 
    calc = Calculator()

    # Basic operations
    assert calc.add(5, 3) == 8
    assert calc.subtract(10, 5) == 5
    assert calc.multiply(2, 3) == 6
    assert calc.divide(10, 2) == 5
    assert calc.divide(10, 0) == "Error: Division by zero is not possible."

    # Advanced operations
    assert calc.square_root(16) == 4
    assert calc.square_root(-1) == "Error: Square root of a negative number is invalid."
    assert calc.exponent(2, 3) == 8
    assert calc.logarithm(100, 10) == 2
    assert calc.logarithm(0) == "Error: Logarithm of non-positive numbers is invalid."

    print("All tests passed.")


# Running the tests
test_calculator()
