# Github Repo Link
# https://github.com/ab12cs34f10/03230320_BIA101_CAP3

# Sunil Yakha
# BBIA
# 03230320

# Rederence:
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/stdtypes.html#str.strip

# Solution Score :  480924

import os  # File existence need to checked by os module as it is imported

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path  # our file path can be stored
        self.result = self.process_file()  # Processing the file can help to istore the result

    def process_file(self):
        result = 0  # Initialize the result to 0
        try:
            with open(self.file_path, 'r') as f:  #  this code helps to Open the file in read mode
                for line in (line.strip() for line in f if line.strip()):  # Iterate through each non-empty line
                    result += self.extract_number(line) 
        except FileNotFoundError:  # If the file is not found it Handle the case 
            print(f"File {self.file_path} not found.")
            result = 0  
        return result  # Final results is shown

    def extract_number(self, line):
        digits = [int(c) for c in line if c.isdigit()] 
        # Return the value calculated from the first and last digit, or 0 if there are less than 2 digits
        return digits[0] * 10 + digits[-1] if len(digits) >= 2 else 0

    def display_result(self):
        print(f"Total sum from file {self.file_path}: {self.result}")  # This code helps to print the results

def execute_program():
    file_name = "03230320_BIA101_CAP3/320.txt"  # file name is defined by this codes
    if file_exists(file_name):  # Is there file  exists, this code checks
        processor = FileProcessor(file_name) 
        processor.display_result()  # Again result is displayed this code
    else:
        print(f"File {file_name} not found.")  # If file is missing, it tells user

def file_exists(file_name):
    return os.path.exists(file_name)  # Return True if the file exists, otherwise False

if __name__ == "__main__":
    execute_program()  # Execute the main program function
