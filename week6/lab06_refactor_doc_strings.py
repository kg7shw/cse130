import json
import math
import matplotlib.pyplot as plt

# Global variables
filename = ""
counter = 0
lengths = []
iterations = []


def get_file():
    """
    Prompts the user to enter the name of the file.
    Returns:
        str: The name of the file entered by the user.
    """
    filename = input("What is the name of the file? ")
    return filename


def read_file(filename):
    """
    Reads the contents of the file.
    Args:
        filename (str): This is the name of the file that will be read.
    Returns:
        file_data (str): The text content of the file.
    """
    try:
        with open(filename, "r") as file:
            file_data = file.read()
        return file_data
    except FileNotFoundError:
        print(f"Unable to open file '{filename}'")
        print("The file was not found. Please make sure the filename is correct.")
    except Exception as e:
        print("An error occurred while reading the file:", str(e))


def load_data(file_data):
    """
    Loads data from the file data as JSON.
    Args:
        file_data (str): The text content of the file.
    Returns:
        list: The list of names extracted from the JSON data.
    """
    try:
        data_json = json.loads(file_data)
        names_list = data_json["array"]
        return names_list
    except json.JSONDecodeError:
        print("There is a problem with loading the JSON data")
        return []
    except Exception as e:
        print("An error occurred while loading the data:", str(e))


def get_search_word():
    """
    Prompts the user to enter the word they are looking for.
    Returns:
        search_word (str): The search word entered by the user.
    """
    search_word = input("What name are we looking for? ")
    return search_word


def binary_search(names_list, search_word):
    """
    Performs the binary search on the names list to find the search word.
    Args:
        names_list (list): The list of names to search in.
        search_word (str): The word the algorithm is searching for.
    Returns:
        found (boolean): True if the search word is found, False otherwise.
    """
    # Initializing variables for binary search
    i_min = 0
    i_max = len(names_list) - 1
    found = False
    global counter

    # Performing binary search on the names list
    while i_min <= i_max and not found:
        counter += 1
        i_middle = math.floor((i_min + i_max) / 2)

        if names_list[i_middle] < search_word:
            i_min = i_middle + 1
        elif names_list[i_middle] > search_word:
            i_max = i_middle - 1
        else:
            found = True

    return found


def run_test_cases(filename, search_word):
    """
    Runs the test cases for binary search.
    Args:
        filename (str): The name of the file to read.
        search_word (str): The word to search for.
    Returns:
        found (boolean): True if the search word is found, False otherwise.
    """
    file_data = read_file(filename)
    names_list = load_data(file_data)
    found = binary_search(names_list, search_word)
    get_efficiency(names_list)
    return found


def test_cases():
    """
    Runs multiple test cases for the binary search algorithm.
    """
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
        test_num += 1
        case_title = case[0]
        filename = case[1]
        search_word = case[2]
        expected_result = case[3]

        print("-----------------------------------")
        print(f"Test Case Number: {test_num}\n")
        found = run_test_cases(filename, search_word)
        
        # Checking if the search word was found and printing the appropriate message
        if expected_result == found:
            result = f"The expected result was: '{expected_result}'\n" \
                     f"The test result was: '{found}'\n" \
                     f"The test result matched expected result.\n" \
                     "The test Passed."
        else:
            result = f"The expected result was: '{expected_result}'\n" \
                     f"The test result was: '{found}'\n" \
                     f"The test result does not match expected result.\n" \
                     "The test Failed."

        print(f"Case Title: {case_title}")
        print(f"Filename: {filename}")
        print(f"Search Word: {search_word}")
        print(f"{result}")
        
        if found:
            print(f"The search word: '{search_word}' was found in '{filename}'.")
        else:
            print(f"The search word: '{search_word}' was not found in '{filename}'.")
        print("-----------------------------------")


def get_efficiency(names_list):
    """
    Calculates and prints the efficiency plot point numbers of the binary search.
    Args:
        names_list (list): The list of names used for searching.
    """
    n = len(names_list)
    c = counter

    lengths.append(n)
    iterations.append(c)

    print("Data points")
    print(f"The length of the list: {n}")
    print(f"How many iterations it took: {c}\n")


def main():
    """
    Runs the program.
    Args:
        none
    Returns:
        none
    """
    test = input("Do you want to run the tests? (y/n): ")
    if test.lower() == 'y':
        test_cases()
    else:
        filename = get_file()
        file_data = read_file(filename)
        names_list = load_data(file_data)
        search_word = get_search_word()
        found = binary_search(names_list, search_word)
        get_efficiency(names_list)

        # Checking if the name was found and printing the appropriate message
        if found:
            print(f"We found {search_word} in {filename}.")
        else:
            print(f"{search_word} was not found in {filename}.")


if __name__ == "__main__":
    main()


plt.plot(lengths, iterations, 'bo-')
plt.xlabel("Length of List")
plt.ylabel("Iterations")
plt.title("Algorithm Efficiency")
plt.show()
