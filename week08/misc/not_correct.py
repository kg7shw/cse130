import json

filename = input("What is the name of the file? ")  # assert: input is not empty

assert filename.strip() != "", "Filename cannot be empty."

try:
    with open(filename, "r") as file:
        file_data = file.read()  # assert: file could not be read or is empty
        assert file_data.strip() != "", "File is empty."

except FileNotFoundError:
    assert False, "File not found."

except IOError:
    assert False, "Error reading the file."

data_json = json.loads(file_data)
data_list = data_json["array"]

assert type(data_list) == list, "Data is not a list."

list_size = len(data_list)
assert list_size > 0, "List is empty."

print(data_list)  # compare with the end result to see if it was sorted correctly

for i_pivot in range(list_size - 1, 0, -1):
    assert 0 <= i_pivot < len(data_list), "Index out of range."

    i_largest = 0

    for i_check in range(1, i_pivot):
        assert 0 <= i_check < len(data_list), "Index out of range."
        if data_list[i_check] > data_list[i_largest]:
            i_largest = i_check

    if data_list[i_largest] > data_list[i_pivot]:
        swap_value = data_list[i_largest]
        data_list[i_largest] = data_list[i_pivot]
        data_list[i_pivot] = swap_value

print(data_list)  # Assert that the data list was actually sorted

assert all(data_list[i] <= data_list[i+1] for i in range(len(data_list)-1)), "List is not sorted."
