# import json

# filename = input("Enter the filename: ")

# with open(filename, 'r') as file:
#     data = file.read()

# data_json = json.loads(data)
# data_list = data_json["array"]

# size = len(data_list)

# for i_sorted in range(size - 1):
#     i_min = i_sorted

#     for i_check in range(i_sorted + 1, size):
#         if int(data_list[i_check]) < int(data_list[i_min]):
#             i_min = i_check

#     if i_min != i_sorted:
#         data_list[i_min], data_list[i_sorted] = data_list[i_sorted], data_list[i_min]

# print("Sorted array:", data_list)
# import json

# filename = input("Enter the filename: ")

# with open(filename, 'r') as file:
#     data = file.read()

# data_json = json.loads(data)
# data_list = data_json["array"]

# size = len(data_list)

# for current_index in range(size - 1, 0, 1):
#     max_index = current_index

#     for compare_index in range(current_index - 1, -1, -1):
#         if int(data_list[compare_index]) > int(data_list[max_index]):
#             max_index = compare_index

#     if max_index != current_index:
#         swap_value = data_list[max_index]
#         data_list[max_index] = data_list[current_index]
#         data_list[current_index] = swap_value

# print(data_list)  # sorted data_list


# import json

# filename = input("Enter the filename: ")
# with open(filename) as file:
#     data_json = json.load(file)
#     data_list = data_json["array"]

# size = len(data_list)

# for i_pivot in range(size - 1, 0, -1):
#     for i_check in range(i_pivot):
#         if int(data_list[i_check]) > int(data_list[i_pivot]):
#             swap_value = data_list[i_check]
#             data_list[i_check] = data_list[i_pivot]
#             data_list[i_pivot] = swap_value

# print(data_list)  # Sorted data_list


import json

# GET filename
filename = input("Enter the filename: ")

# READ file
with open(filename, "r") as file:
    file_content = file.read()

# data_json = json.loads(file)
data_json = json.loads(file_content)

# data_list = data_json["array"]
data_list = data_json["array"]

# size = length(data_list)
size = len(data_list)

# FOR i_pivot = size - 1 DOWN TO 0
for i_pivot in range(size - 1, -1, -1):
    # FOR i_check = 0 UP TO i_pivot
    for i_check in range(i_pivot + 1):
        # IF parse int(data_list[i_check]) > parse int(data_list[i_pivot])
        if int(data_list[i_check]) > int(data_list[i_pivot]):
            # swap_value = data_list[i_check]
            swap_value = data_list[i_check]
            # data_list[i_check] = data_list[i_pivot]
            data_list[i_check] = data_list[i_pivot]
            # data_list[i_pivot] = swap_value
            data_list[i_pivot] = swap_value

# PUT data_list
print(data_list)

