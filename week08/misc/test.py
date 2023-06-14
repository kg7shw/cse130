import json

filename = input("What is the name of the file? ")

with open(filename, "r") as file:
    file_data = file.read()

data_json = json.loads(file_data)
data_list = data_json["array"]

print(data_list)

# Convert elements in data_list to integers
# data_list = [int(x) for x in data_list]

for i_pivot in range(len(data_list) - 1, -1, -1):
    i_largest = 0

    for i_check in data_list:
        if data_list[i_check] > data_list[i_largest]:
            i_largest = i_check
    
    if data_list[i_largest] > data_list[i_pivot]:
        data_list[i_largest], data_list[i_pivot] = data_list[i_pivot], data_list[i_largest]

# Convert elements in data_list back to strings for printing
# data_list = [str(x) for x in data_list]

print(data_list)
# Lab08.languages.json