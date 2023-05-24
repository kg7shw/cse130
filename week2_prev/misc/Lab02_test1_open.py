import json

def read_file(file_name):
    try:
        file_handle = open(file_name)
        data_text = file_handle.read()
        file_handle.close()
        return data_text
    # except FileNotFoundError:
    #     print(f"Error: The {file_name} file was not found.")
    # except PermissionError:
    #     print(f"Error: You do not have permission to read {file_name}.")
    except: 
        print(f"There was an error.\nUnable to open file {file_name}.")

def load_json(data_text):
    try:
        data_json = json.loads(data_text)
        return data_json
    except:
        print("There is a problem with loading the json data")

def get_lists(data_json):
    usernames_list = data_json["username"]
    passwords_list = data_json["password"]
    return usernames_list, passwords_list

def make_dictionary(usernames_list, passwords_list):
    user_lookup_dict = dict(zip(usernames_list, passwords_list))
    return user_lookup_dict

def get_user_input():  
    username_input = input("username: ")
    password_input = input("password: ")
    return username_input, password_input

def authenticate_user(username_input, password_input, user_lookup_dict):
    if username_input in user_lookup_dict:
        if user_lookup_dict[username_input] == password_input:
            return "You're authenticated"
        
    return "You are not authorized to use the system."

def run_test_case(user_lookup_dict):
    
    test_cases = [
    ["Incorrect username", "John Cheese", "None shall pass", "You are not authorized to use the system."],
    ["Incorrect password", "Black Knight", "Tis but a scratch.", "You are not authorized to use the system."],
    ["Both incorrect", "John Cheese", "Tis but a scratch.", "You are not authorized to use the system."],
    ["Wrong Index", "King Arthur", "Bring out your dead!", "You are not authorized to use the system."],
    ["Valid Black Knight", "Black Knight", "None shall pass", "You're authenticated"],
    ["Valid King Arthur", "King Arthur", "Run away!", "You're authenticated"],
    ["Valid French Soldier", "French Soldier", "I fart in your general direction", "You're authenticated"]
]

    for case in test_cases:
        title_test = case[0]
        username_test = case[1]
        password_test = case[2]
        expected_result_test = case[3]

        auth = authenticate_user(username_test, password_test, user_lookup_dict)
        

        if expected_result_test == auth:
            result = "Pass"
        else:
            result = "case does not match expected result"
    
        print(f"\n{title_test}\nUsername: {username_test}\nPassword:{password_test}\n{auth}\n{result}\n")
    

def main():
    file_name = 'Lab01.json'
    data_text = read_file(file_name)
    data_json = load_json(data_text)
    usernames_list, passwords_list =  get_lists(data_json)
    user_lookup_dict = make_dictionary(usernames_list, passwords_list)
    # username_input, password_input = get_user_input()
    # auth = authenticate_user(username_input, password_input, user_lookup_dict)
    run_test_case(user_lookup_dict)
    # print(auth)



    
   
    
    

if __name__ == "__main__":
    main()
