import functools
import time

# Step 1: Custom Decorators

def log_decorator(func):
    """Decorator to log function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Calling function: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def time_decorator(func):
    """Decorator to time function execution"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[TIME] Function {func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper

def access_control_decorator(user_role):
    """Decorator to restrict access to certain roles"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user_role != 'admin':
                print("[ACCESS DENIED] User does not have the required privileges.")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_decorator
@time_decorator
@access_control_decorator(user_role='admin')  # Change to 'user' for access denial
def example_function(a, b):
    """Example function that adds two numbers"""
    print(f"Addition: {a} + {b} = {a + b}")
    return a + b

# Step 2: Call Count Decorator

def call_count_decorator(func):
    """Decorator to track how many times a function has been called"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"[CALL COUNT] Function {func.__name__} has been called {wrapper.call_count} times.")
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper

@call_count_decorator
def sample_function():
    """A sample function to demonstrate call count tracking"""
    print("Function executed.")

# Step 3: Metaclass with Constraints

class EnforceAttributes(type):
    """Metaclass to enforce specific attributes and methods"""
    def __new__(cls, name, bases, class_dict):
        if 'name' not in class_dict:
            raise TypeError(f"Class {name} must have a 'name' attribute.")
        if 'greet' not in class_dict or not callable(class_dict['greet']):
            raise TypeError(f"Class {name} must have a callable 'greet' method.")
        return super().__new__(cls, name, bases, class_dict)

class Person(metaclass=EnforceAttributes):
    name = "John"
    
    def greet(self):
        print(f"Hello, my name is {self.name}.")



# Step 4: Metaclass with Class Registry

class RegistryMeta(type):
    """Metaclass to automatically register classes"""
    registry = {}

    def __new__(cls, name, bases, class_dict):
        new_class = super().__new__(cls, name, bases, class_dict)
        cls.registry[name] = new_class
        return new_class

    @classmethod
    def get_class(cls, name):
        return cls.registry.get(name)

class Animal(metaclass=RegistryMeta):
    pass

class Dog(Animal):
    def speak(self):
        return "Barks!"

class Cat(Animal):
    def speak(self):
        return "Meows!"

# Running Examples with Clean Output

print("\n=== Step 1: Custom Decorators ===")
result = example_function(5, 10)  # Admin role granted

print("\n=== Step 2: Function Call Count Decorator ===")
sample_function()
sample_function()
sample_function()

print("\n=== Step 3: Metaclass with Attribute Enforcement ===")
person = Person()
person.greet()

# Example of a class with a missing 'greet' method
print("\n=== Attempting to define InvalidAnimal ===")
try:
    class InvalidAnimal(metaclass=EnforceAttributes):
        name = "Unknown"  # This class lacks a 'greet' method
except TypeError as e:
    print(f"[ERROR] {e}")

print("\n=== Step 4: Metaclass with Registry ===")
print(f"Registered Classes: {RegistryMeta.registry}")
dog_class = RegistryMeta.get_class('Dog')
dog = dog_class()
print(f"The Dog: {dog.speak()}")
