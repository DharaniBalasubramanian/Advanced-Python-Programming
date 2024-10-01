#  4.2 Create a File Parser with Error Handling
# - Objective: Develop a program that reads and processes files, handling errors gracefully.
# - Instructions:
#   - Step 1: Create a program that reads a CSV file and processes its contents (e.g., summing numeric columns, extracting specific data).
#   - Step 2: Implement error handling for common file-related issues, such as file not found, incorrect format, and permission errors.
#   - Step 3: Extend the program to handle different file formats (e.g., JSON, XML) and implement corresponding error handling.
#   - Step 4: Implement a logging mechanism to record errors and warnings to a log file.
# - Expected Output: A file processing program that can handle various file formats and errors, with logs documenting the handling of exceptional cases.



import csv
import json
import xml.etree.ElementTree as ET
import logging
import os

# Setting up logging to record errors and warnings
logging.basicConfig(filename='file_parser.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# data to be used in files
data = [
    {"name": "Vinitha", "age": 25, "salary": 50000},
    {"name": "Akshitha", "age": 24, "salary": 40000},
    {"name": "Amirtha", "age": 27, "salary": 100000}
]

# Create files in CSV, JSON, and XML extensions
def create_files():
    try:
        # Create CSV file
        with open('data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Salary"])  # Writing headers
            for entry in data:
                writer.writerow([entry["name"], entry["age"], entry["salary"]])
        
        # Create JSON file
        with open('data.json', 'w') as file:
            json_data = {"employees": data}
            json.dump(json_data, file, indent=4)

        # Create XML file
        root = ET.Element("employees")
        for entry in data:
            employee = ET.SubElement(root, "employee")
            employee.set("name", entry["name"])
            employee.set("age", str(entry["age"]))
            employee.set("salary", str(entry["salary"]))
        tree = ET.ElementTree(root)
        tree.write('data.xml')

        print("Sample files created successfully.")

    except Exception as e:
        logging.error(f"Error creating sample files: {e}")

# Function to process CSV files
def process_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            total_salary = 0
            for row in reader:
                total_salary += int(row['Salary'])
            print(f"Total Salary (CSV): {total_salary}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except PermissionError:
        logging.error(f"Permission denied: {file_path}")
    except Exception as e:
        logging.error(f"Error processing CSV: {e}")

# Function to process JSON files
def process_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            total_salary = sum(emp['salary'] for emp in data['employees'])
            print(f"Total Salary (JSON): {total_salary}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logging.error(f"Incorrect JSON format in file: {file_path}")
    except PermissionError:
        logging.error(f"Permission denied: {file_path}")
    except Exception as e:
        logging.error(f"Error processing JSON: {e}")

# Function to process XML files
def process_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        total_salary = 0
        for employee in root.findall('employee'):
            total_salary += int(employee.get('salary'))
        print(f"Total Salary (XML): {total_salary}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except ET.ParseError:
        logging.error(f"Incorrect XML format in file: {file_path}")
    except PermissionError:
        logging.error(f"Permission denied: {file_path}")
    except Exception as e:
        logging.error(f"Error processing XML: {e}")

# Main function to handle different file formats
def process_file(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File does not exist: {file_path}")
        return

    if file_path.endswith('.csv'):
        process_csv(file_path)
    elif file_path.endswith('.json'):
        process_json(file_path)
    elif file_path.endswith('.xml'):
        process_xml(file_path)
    else:
        logging.error(f"Unsupported file format: {file_path}")

# Driver function
if __name__ == "__main__":
    # Step 1: Create sample files
    create_files()

    # Step 2: Process files and handle errors
    process_file('data.csv')  # Process CSV
    process_file('data.json')  # Process JSON
    process_file('data.xml')  # Process XML

    # Example of handling non-existent or incorrect file
    process_file('non_existent_file.xlsx')
    process_file('data.txt') 
