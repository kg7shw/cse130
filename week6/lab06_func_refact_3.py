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


def read_file(filename):
    """READ FILE : open the file and return the text of the file"""
    try:
        with open(filename, "r") as file:
            file_data = file.read()
        return file_data
    except:
        print(f"Unable to open file '{filename}'")
        print("The file was not found it is most likely not spelled correctly.")


def load_data(file_data):
    # Parsing the file data as JSON
    try:
        data_json = json.loads(file_data)
        names_list = data_json["array"]
        return names_list
    except:
        print("There is a problem with loading the json data")
        return []


def get_seachword():
    # Prompting the user to enter the name they are looking for
    search_word = input("What name are we looking for? ")
    return search_word


def binary_search(names_list, search_word):
    # Initializing variables for binary search
    i_min = 0
    i_max = len(names_list) - 1
    found = False

    # Performing binary search on the names list
    while i_min <= i_max and not found:
        i_middle = math.floor((i_min + i_max) / 2)

        if names_list[i_middle] < search_word:
            i_min = i_middle + 1
        elif names_list[i_middle] > search_word:
            i_max = i_middle - 1
        else:
            found = True
    return found

def run_test_cases(filename, search_word):
    file_data = read_file(filename)
    names_list = load_data(file_data)
    found = binary_search(names_list, search_word)

    # Checking if the name was found and printing the appropriate message
    if found:
        print(f"We found {search_word} in {filename}.")
    else:
        print(f"{search_word} was not found in {filename}.")

    return found

def test_cases():
    # Case[0] File[1] Search Word[2] Found[3]
    test_cases = [
        ["Empty list", "Lab06.empty.json", "Empty", False],
        ["Single item found", "Lab06.trivial.json", "trivial", True],
        ["Single item not found", "Lab06.trivial.json", "missing", False],
        ["Small list found", "Lab06.languages.json", "C++", True],
        ["Small list not found", "Lab06.languages.json", "Lisp", False],
        ["Big list found", "Lab06.countries.json", "United States of America", True],
        ["Big list not found", "Lab06.countries.json", "United States", False]
    ]
    
    
    test_num = 0
    for case in test_cases:
        # filename = ""
        test_num += 1
        case_title = case[0]
        filename = case[1]
        search_word = case[2]
        expected_result = case[3]
        found = run_test_cases(filename, search_word)

        # Checking if the search word was found and printing the appropriate message
        if expected_result == found:
            result = f"The expected result was: {expected_result}\nThe test result was: {found}\nThe test result matched expected result. \nThe test Passed."
        else:
            result = f"The expected result was: {expected_result}\nThe test result was: {found}\nThe test result does not match expected result. \nThe test Failed."

        print(f"\nTest Case Number: {test_num}")
        print(f"\nCase Title: {case_title}")
        print(f"Filename: {filename}")
        print(f"Search Word: {search_word}")
        print(f"{result}\n")


def main():
    test = input("Do you want to run the tests? (y/n): ")
    if test.lower() == 'y':
        test_cases()
    else:
        filename = get_file()
        file_data = read_file(filename)
        names_list = load_data(file_data)
        search_word = get_seachword()
        found = binary_search(names_list, search_word)

        # Checking if the name was found and printing the appropriate message
        if found:
            print(f"We found {search_word} in {filename}.")
        else:
            print(f"{search_word} was not found in {filename}.")


if __name__ == "__main__":
    main()
