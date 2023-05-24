# 1. Name:
#      Grant Call
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program is designed to facilitate searching for a specific name
#      within the contents of a file. It prompts the user to enter a filename
#      and proceeds to read the file's contents, storing them in a list.
#      The user is then prompted to enter a name. Afterwards, the program
#      determines whether the entered name exists within the list of file
#      contents and provides the user with the corresponding result.
# 4. Algorithmic Efficiency
#      -Identify the algorithmic efficiency and tell why it is as you say it is-
# 5. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 6. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

# Importing the necessary libraries
import json
import math

# initialize global variables
filename = ""


def get_file():
    filename = input("What is the name of the file? ")
    return filename

def open_file(filename):
    # Opening the file and reading its contents
    with open(filename, "r") as file:
        file_data = file.read()

    # Parsing the file data as JSON
    data_json = json.loads(file_data)
    names_list = data_json["array"]
    return names_list

def get_seachword():
    # Prompting the user to enter the name they are looking for
    element = input("What name are we looking for? ")
    return element

def binary_search(names_list, element):
    # Initializing variables for binary search
    i_min = 0
    i_max = len(names_list) - 1
    found = False

    # Performing binary search on the names list
    while i_min <= i_max and not found:
        i_middle = math.floor((i_min + i_max) / 2)

        if names_list[i_middle].lower() < element:
            i_min = i_middle + 1
        elif names_list[i_middle].lower() > element:
            i_max = i_middle - 1
        else:
            found = True
    return found


def main():

    filename = get_file()
    names_list = open_file(filename)
    element = get_seachword().lower()
    found = binary_search(names_list, element)

    # Checking if the name was found and printing the appropriate message
    if found:
        print(f"We found {element} in {filename}.")
    else:
        print(f"{element} was not found in {filename}.")