# Sources:
# https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
# Loading a JSON File in Python – How to Read and Parse JSON
# https://www.w3schools.com/python/python_try_except.asp
# https://www.w3schools.com/python/python_functions.asp
# https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/
# https://www.w3schools.com/python/ref_func_zip.asp





import json

# Check if the file can open. If it can't open it will throw FileNotFoundError.
with open("Lab02.json") as data_file_handle:
    data_text = data_file_handle.read()


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
# def authenticate_user():
def authenticate(username, password):
    if username in user_lookup_dict:
        if user_lookup_dict[username] == password:
            return "Authenticated"
    return "Not authenticated"





# def test_cases ():
