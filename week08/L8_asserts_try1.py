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

# Lab08.languages.json


# Assert the list are sorted
# Assert the file
# Assert the data type
# Assert index out of range
# assert empty list
# Assert anything else that is needed


import json

filename = input("what is the name of the file? ")

try:
    with open(filename, "r") as file:
        file_data = file.read()
except:
    print(f"Unable to open file '{filename}'.")
    print("The file was not found it is most likely not spelled correctly")
    print("Or the file does not exist.")

data_json = json.loads(file_data)
data_list = data_json["array"]
assert type(data_list) == list # datalist is not a list

list_size = len(data_list) 
assert list_size > 0 # The List is Empty

print(data_list) # this is here to compare with the end result to see if it was sorted correctly

for i_pivot in range(list_size - 1, 0, -1):
    assert 0 <= i_pivot < len(data_list) # Index out of range.
    i_largest = 0

    for i_check in range(1, i_pivot):
        assert 0 <= i_check < len(data_list) # Index out of range.
        if data_list[i_check] > data_list[i_largest]:
            i_largest = i_check
    
    if data_list[i_largest] > data_list[i_pivot]:
        swap_value = data_list[i_largest]
        data_list[i_largest] = data_list[i_pivot]
        data_list[i_pivot] = swap_value

print(data_list) # Assert that the datalist was actually sorted
