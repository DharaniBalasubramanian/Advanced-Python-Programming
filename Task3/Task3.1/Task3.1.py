#Task 3: Functional Programming

#  3.1 Data Processing with Map, Filter, Reduce
# - Objective: Learn to apply functional programming techniques for efficient data processing.
# - Instructions:
#   - Step 1: Given a list of student records (dictionaries with attributes like `name`, `age`, `grades`), use `map` to extract specific fields (e.g., a list of student names).
#   - Step 2: Use `filter` to create a sublist of students who passed a particular course (e.g., grades above a threshold).
#   - Step 3: Use `reduce` to calculate the total sum of grades or to determine the highest grade among all students.
#   - Step 4: Chain these operations together to perform complex data processing in a single line of code.
# - Expected Output: Efficiently processed data using functional programming techniques, demonstrated through the use of `map`, `filter`, and `reduce`.



from functools import reduce
# student record data in list of dictionary
students = [
    {'name': 'Akila', 'age': 25, 'grades': [100, 90, 95, 99, 100]},
    {'name': 'Anusha', 'age': 21, 'grades': [90, 90, 70, 40, 10]},
    {'name': 'Bhavatha', 'age': 26, 'grades': [11, 30, 20, 12, 34]},
    {'name': 'Vishali', 'age': 24, 'grades': [90, 100, 100, 99, 98]}
]

# function to perform the sum of all grades of a student
def total_grades(grades):
    return reduce(lambda x, y: x + y, grades)

Data = {
# Mapping to extract specific student records
    'student_names' : list(map(lambda student: student['name'], students)),
    'ages' : list(map(lambda student: student['age'], students)),
    'grades' : list(map(lambda student: student['grades'], students)),

# Filtering passing students with average of grades > 50
    'passing_students' : list(map(lambda student: student['name'],
                filter(lambda student: all(grade > 50 for grade in student['grades']), students))),

# Filtering students with atleast one grade < 50 (failed in atleast one subject)
    'below_50' : list(map(lambda student: student['name'], filter(lambda student: any(grade < 50 for grade in student['grades']), students))),

# To store the sum of grades in a list
    'total_grades' : list(map(lambda student: total_grades(student['grades']), students)),

# Has List of each student with their total marks obtained
    'students_total_grades': {student['name']: total_grades(student['grades']) for student in students},

# finds the topper 
    'topper' : max(students, key=lambda student: total_grades(student['grades']))['name']
}

# Output
print("Student Names:", Data['student_names'])
print("Passing Students:", Data['passing_students'])
print("Failed Students:", Data['below_50'])
print("Final Score:-")

# Print each student's total grades
for name, total in Data['students_total_grades'].items():
    print(f"{name} : {total}")

print(f"The topper is", Data["topper"])
