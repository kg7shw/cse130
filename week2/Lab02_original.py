# Sources:
# https://docs.python.org/3/library/functions.html#open
# https://www.w3schools.com/python/python_try_except.asp
# https://www.w3schools.com/python/python_functions.asp
# https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/
# https://www.w3schools.com/python/ref_func_zip.asp
# https://www.freecodecamp.org/news/python-try-and-except-statements-how-to-handle-exceptions-in-python/




import json

# Check if the file can open. If it can't open it will throw FileNotFoundError.
with open("Lab02.json") as data_file_handle:
    data_text = data_file_handle.read()

# data_file_handle = open("Lab02.json")
# data_text = data_file_handle.read()
# data_file_handle.close()


# Convert the json file data into two different lists.
try:
    data_json = json.loads(data_text)
    usernames_list = data_json["username"]
    passwords_list = data_json["password"]
except:
    print("There is a problem with loading the json data")

user_lookup_dict = dict(zip(usernames_list, passwords_list))
print(user_lookup_dict)

# Check if the user has access to the system of not.

username = input("username: ")
password = input("password: ")

if username in user_lookup_dict:
    if user_lookup_dict[username] == password:
        print("You're authenticated")

else:
    print("You are not authorized to use the system.")





