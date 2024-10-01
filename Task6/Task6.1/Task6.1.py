import csv
import json
import xml.etree.ElementTree as ET

# Custom exception for unsupported file formats
class UnsupportedFileFormatError(Exception):
    """Custom exception for unsupported file formats."""
    pass

# Function to process CSV files
def process_csv(input_file, output_file, age_threshold):
    try:
        print(f"Step 1: Opening CSV file '{input_file}' for reading.")
        with open(input_file, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)
            print(f"Step 2: Reading CSV file and filtering rows where Age > {age_threshold}.")

            with open(output_file, mode='w', newline='') as outfile:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                filtered_rows = 0

                for row in reader:
                    if int(row['Age']) > age_threshold:
                        writer.writerow(row)
                        filtered_rows += 1

        print(f"Step 3: Filtered {filtered_rows} rows. Output written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to process JSON files
def process_json(input_file, output_file, age_threshold):
    try:
        print(f"Step 1: Opening JSON file '{input_file}' for reading.")
        with open(input_file, mode='r') as infile:
            data = json.load(infile)
            print(f"Step 2: Reading JSON data and filtering records where Age > {age_threshold}.")
            
            filtered_data = [record for record in data if int(record['Age']) > age_threshold]

            with open(output_file, mode='w') as outfile:
                json.dump(filtered_data, outfile, indent=4)
        
        print(f"Step 3: Filtered {len(filtered_data)} records. Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to process XML files
def process_xml(input_file, output_file, age_threshold):
    try:
        print(f"Step 1: Opening XML file '{input_file}' for reading.")
        with open(input_file, mode='r') as infile:
            tree = ET.parse(infile)
            root = tree.getroot()

            print(f"Step 2: Reading XML data and removing <person> elements where Age <= {age_threshold}.")
            removed_count = 0
            for person in root.findall('person'):
                age = int(person.find('age').text)
                if age <= age_threshold:
                    root.remove(person)
                    removed_count += 1

            with open(output_file, mode='wb') as outfile:
                tree.write(outfile)

        print(f"Step 3: Removed {removed_count} elements. Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to determine the file format and process accordingly
def process_file(input_file, output_file, age_threshold, file_format):
    try:
        print(f"Starting file processing for format: {file_format.upper()}")
        if file_format == 'csv':
            process_csv(input_file, output_file, age_threshold)
        elif file_format == 'json':
            process_json(input_file, output_file, age_threshold)
        elif file_format == 'xml':
            process_xml(input_file, output_file, age_threshold)
        else:
            raise UnsupportedFileFormatError(f"Unsupported file format: {file_format}")

    except UnsupportedFileFormatError as e:
        print(e)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Process CSV
    process_file('input.csv', 'output.csv', age_threshold=30, file_format='csv')

    # Process JSON
    process_file('input.json', 'output.json', age_threshold=30, file_format='json')

    # Process XML
    process_file('input.xml', 'output.xml', age_threshold=30, file_format='xml')
