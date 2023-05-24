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

# Prompting the user to enter the name of the file
filename = input("What is the name of the file? ")

# Opening the file and reading its contents
with open(filename, "r") as file:
    file_data = file.read()

# Parsing the file data as JSON
data_json = json.loads(file_data)
names_list = data_json["array"]

# Prompting the user to enter the name they are looking for
search_word = input("What name are we looking for? ")
element = search_word.lower()

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



