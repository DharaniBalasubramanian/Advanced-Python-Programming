#  3.2 Create Custom Decorators
# - Objective: Understand and create decorators to modify the behavior of functions.
# - Instructions:
#   - Step 1: Create a simple decorator called `timing_decorator` that measures and prints the execution time of a function.
#   - Step 2: Create a `logger_decorator` that logs the input arguments and output results of a function call.
#   - Step 3: Apply multiple decorators to a function and observe the combined effects.
#   - Step 4: Create a parameterized decorator that allows passing arguments to control its behavior (e.g., `@repeat(n)` to repeat a function `n` times).
# - Expected Output: A set of custom decorators that modify and enhance the behavior of functions, along with examples demonstrating their use.



import time

# Applying timing_decorator to measure the execution time of function
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # to record start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # to record end time
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)  # Simulates a function that takes 1 second to execute
    return "Done"


# Applying logger_decorator to log input and output of function with 2 arguments
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: ({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Output from {func.__name__} function: {result}")
        return result
    return wrapper

# Applying Multiple decorators to a function - this works in order 
@timing_decorator # second
@logger_decorator # first
def add(a, b, c):
    return a + b + c

# Applying Parameterized decorator to repeat the function n times
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# Testing the decorators
print("Executing Timing Decorator:-")
slow_function()
print("Executing Multiple Decorators:-")
add(4, 10, 5)  
print("--------------------------------------------------")
print("Executing Parameteraized Decorator:-")
greet("Dharani")  
