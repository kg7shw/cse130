import json

# Check if the file can open. If it can't open it will throw FileNotFoundError.
# Add function here
with open("Lab02.json") as data_file_handle:
    data_text = data_file_handle.read()

# Convert the json file data into two different lists.
# Add function here
try:
    data_json = json.loads(data_text)
    usernames_list = data_json["username"]
    passwords_list = data_json["password"]
except:
    print("There is a problem with loading the json data")

# Add function here
user_lookup_dict = dict(zip(usernames_list, passwords_list))
print(user_lookup_dict)

# Check if the user has access to the system of not.
# def authenticate_user():
# Add function here
def authenticate(username, password):
    if username in user_lookup_dict:
        if user_lookup_dict[username] == password:
            return "Authenticated"
    return "Not authenticated"