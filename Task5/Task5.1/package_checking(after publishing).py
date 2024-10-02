
# Import the package and its modules
import my_utilities_dharanib282000
from my_utilities_dharanib282000 import add, subtract
from my_utilities_dharanib282000 import read_file

# Using the math operations
result_add = add(2, 3)
result_subtract = subtract(5, 3)

# Using file operation (assuming 'example.txt' exists)
try:
    file_content = read_file('example.txt')
except FileNotFoundError:
    file_content = "File not found."

# Print the results
print(f"Addition: 2 + 3 = {result_add}")
print(f"Subtraction: 5 - 3 = {result_subtract}")
print(f"File content: {file_content}")
