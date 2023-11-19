# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Jenna Ho,11/19/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

'''
a class for all inputs and outputs of student data
'''


class IO:
    '''
    print out error message
    '''
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message)
        print(error.__doc__)
        print(error.__str__())
    '''
    print out menu
    '''
    @staticmethod
    def output_menu(menu: str):
        print(menu)
    '''
    print out menu choice
    '''
    @staticmethod
    def input_menu_choice():
        menu_choice = input("What would you like to do: ")
        return menu_choice
    # return back to where it is called, and input in variable:menu choice
    '''
    taking entire student data list and printing it out
    '''
    @staticmethod
    def output_student_courses(student_data: list):
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
    '''
    add student into student list
    '''
    @staticmethod
    def input_student_data(student_data: list, student):
        student_data.append(student)
    # added student into student_data


'''
this class reads the file and inputs the student data, writes student data to the file
'''


class FileProcessor:
    # instance variables: properties of the class
    def __init__(self):
        self.io = IO()

    # read from the file and put it in the student list
    @staticmethod
    def read_data_from_file(self, file_name: str, data: list):
        try:
            file = open(file_name, "r")

            # JSON Answer
            data = json.load(file)

            file.close()
            return data
        except Exception as e:
            self.io.output_error_messages("there is a problem with reading the file", e)
            # e.doc---explain the reason of the mistake/ str--convert exception into readable format
        finally:
            if file.closed == False:
                file.close()
    '''
    write student list to the file
    added self to call the instance variable within its own class
    '''
    @staticmethod
    def write_data_to_file(self, file_name: str, student_data: list):
        try:
            file = open(file_name, "w")

            # # JSON answer-- writes the student to the file
            json.dump(student_data, file)

            file.close()
            print("The following data was saved to file!")
            self.io.output_student_courses(student_data)
        except Exception as err:
            if file.closed == False:
                file.close()
                self.io.output_error_messages('there is an error reading the file', err)


# define functions

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

# to call read data from file function
fileprocessor = FileProcessor()
students = fileprocessor.read_data_from_file(fileprocessor, file_name=FILE_NAME, data=students)
# make the class object and be able to call it
io = IO()
# Present and Process the data
while (True):

    # Present the menu of choices-- Call out menu using function2
    io.output_menu(MENU)
    menu_choice = io.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            # students.append(student_data)
            io.input_student_data(students, student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            io.output_error_messages('there are numbers in your input', e)
        except Exception as e:
            io.output_error_messages('There was a problem with your entered data', e)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        io.output_student_courses(students)
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        fileprocessor.write_data_to_file(fileprocessor, FILE_NAME, students)
        continue

        # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

    print("Program Ended")
# inside () are parameters - what I want to pass to the function