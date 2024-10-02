# Python code with bugs in data processing - no debugging and logging
import csv

def read_csv(file_path):         # Lack of error handling for File Not Found error
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    processed = []
    for row in data:
        result = sum([int(item) for item in row])  # Assuming all elements are numbers
        processed.append(result)
    return processed

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Processed Results"])
        for row in data:
            writer.writerow([row])

# Main pipeline
data = read_csv("data.csv")
processed_data = process_data(data)
write_csv("processed_data.csv", processed_data)
