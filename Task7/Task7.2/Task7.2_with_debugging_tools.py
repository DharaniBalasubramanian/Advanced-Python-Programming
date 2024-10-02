import csv
import logging

logging.basicConfig(level=logging.DEBUG)

def read_csv(file_path):
    """Reads a CSV file and returns the data as a list of rows. Also include error handling, logging"""
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                logging.debug(f"Reading row: {row}")
                data.append(row)
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        return []
    return data


def process_row(row):
    """Helper function: Processes a individual row by summing numeric values. Also includes error handling, logging"""
    try:
        result = sum([int(item) for item in row if item])  # Ignore empty items
    except ValueError:
        logging.error(f"Non-numeric data found in row: {row}")
        return None  # Return None to indicate error
    return result

def process_data(data):
    """Processes the entire dataset by summing values in each row."""
    processed = []
    for row in data:
        result = process_row(row)
        if result is not None:
            processed.append(result)
    return processed

def write_csv(file_path, data):
    """Writes processed data to a CSV file."""
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Processed Results"])
        for row in data:
            writer.writerow([row])

# Main pipeline
def main():
    input_file = "data.csv"
    output_file = "processed_data.csv"
    
    data = read_csv(input_file)
    if data:         # for empty file
        processed_data = process_data(data)
        write_csv(output_file, processed_data)
        logging.info(f"Processed data written to {output_file}")
    else:
        logging.error("No data to process.")

if __name__ == "__main__":
    main()
