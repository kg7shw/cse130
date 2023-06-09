import json

filename = input("what is the name of the file? ")

# Lab08.languages.json


with open(filename, "r") as file:
    file_data = file.read()

data_json = json.loads(file_data)
data_list = data_json["array"]

print(data_list)

for i_pivot in range(len(data_list) -1, -1 -1 ):
    i_largest = 0

    for i_check in range(i_pivot + 1):
        if data_list[i_check] > data_list[i_largest]:
            i_largest = i_check
    
    if data_list[i_largest] > data_list[i_pivot]:
        swap_value = data_list[i_largest]
        data_list[i_largest] = data_list[i_pivot]
        data_list[i_pivot] = swap_value

print(data_list)



# import json

# filename = input("What is the name of the file? ")

# with open(filename, "r") as file:
#     file_data = file.read()

# data_json = json.loads(file_data)
# data_list = data_json["array"]

# print(data_list)

# for i_pivot in range(len(data_list) - 1, -1, -1):
#     i_largest = 0

#     for i_check in range(1, i_pivot + 1):
#         if data_list[i_check] > data_list[i_largest]:
#             i_largest = i_check

#     if data_list[i_largest] > data_list[i_pivot]:
#         swap_value = data_list[i_largest]
#         data_list[i_largest] = data_list[i_pivot]
#         data_list[i_pivot] = swap_value

# print(data_list)


# import json

# filename = input("What is the name of the file? ")

# with open(filename, "r") as file:
#     file_data = file.read()

# data_json = json.loads(file_data)
# data_list = data_json["array"]

# print(data_list)

# for i_pivot in range(len(data_list) - 1, -1, -1):
#     i_largest = 0

#     for i_check in range(1, i_pivot + 1):
#         if data_list[i_check] > data_list[i_largest]:
#             i_largest = i_check

#     if data_list[i_largest] > data_list[i_pivot]:
#         swap_value = data_list[i_largest]
#         data_list[i_largest] = data_list[i_pivot]
#         data_list[i_pivot] = swap_value

# print(data_list)
