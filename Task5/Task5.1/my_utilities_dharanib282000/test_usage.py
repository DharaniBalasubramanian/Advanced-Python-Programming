from my_utilities_dharanib282000 import (
    add,
    subtract,
    multiply,
    divide,
    capitalize_words,
    reverse_string,
    count_vowels,
    read_file,
    write_file
)

def main():
    # Testing Mathematical Operations
    print("Mathematical Operations:")
    print("Addition: 2 + 3 =", add(2, 3))                          
    print("Subtraction: 5 - 2 =", subtract(5, 2))                  
    print("Multiplication: 3 * 4 =", multiply(3, 4))  
    try:             
        print("Division: 10 / 2 =", divide(10, 2))                 
        print("Division: 10 / 0 =", divide(10, 0))                 
    except ValueError as e:
        print("Error:", e)

    # Testing String Operations
    print("\nString Operations:")
    print("Capitalize Words:", capitalize_words("hello world"))     
    print("Reverse String:", reverse_string("hello"))                
    print("Count Vowels in 'hello':", count_vowels("hello"))       
    # Testing File Operations
    file_path = 'test.txt'
    write_file(file_path, "Hello, World!")                          
    print("Written to file:", file_path)

    # Reading from the file
    content = read_file(file_path)                                  
    print("File Content:", content)                                  

if __name__ == '__main__':
    main()
