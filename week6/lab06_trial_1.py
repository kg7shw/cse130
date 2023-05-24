import json
import math

filename = input("What is the name of the file? ")

with open(filename, "r") as file:
    file_data = file.read()

data_json = json.loads(file_data)
names_list = data_json["array"]

element = input("What name are we looking for? ").lower()


i_min = 0
i_max = len(names_list) - 1
found = False

while i_min <= i_max and not found:
    i_middle = math.floor((i_min + i_max) / 2)

    if names_list[i_middle].lower() < element:
        i_min = i_middle + 1
    elif names_list[i_middle].lower() > element:
        i_max = i_middle - 1
    else:
        found = True

if found:
    print(f"We found {element.capitalize()} in {filename}.")
else:
    print(f"{element.capitalize()} was not found in {filename}.")
