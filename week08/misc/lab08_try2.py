# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

filename = input("what is the name of the file? ")

# Lab08.languages.json

with open(filename, "r") as file:
    file_data = file.read()

data_json = json.loads(file_data)
data_list = data_json["array"]
list_size = len(data_list)

print(data_list)

for i_pivot in range(list_size - 1, 0, -1):
    i_largest = 0

    for i_check in range(1, i_pivot):
        if data_list[i_check] > data_list[i_largest]:
            i_largest = i_check
    
    if data_list[i_largest] > data_list[i_pivot]:
        swap_value = data_list[i_largest]
        data_list[i_largest] = data_list[i_pivot]
        data_list[i_pivot] = swap_value

print(data_list)