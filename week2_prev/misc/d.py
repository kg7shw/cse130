test_cases = [
["Incorrect username", "John Cheese", "None shall pass", "Not authenticated"],
["Incorrect password", "Black Knight", "Tis but a scratch.", "Not authenticated"],
["Both incorrect", "John Cheese", "Tis but a scratch.", "Not authenticated"],
["Wrong Index", "King Arthur", "Bring out your dead!", "Not authenticated"],
["Valid Black Knight", "Black Knight", "None shall pass", "Authenticated"],
["Valid King Arthur", "King Arthur", "Run away!", "Authenticated"],
["Valid French Soldier", "French Soldier", "I fart in your general direction", "Authenticated"]
]

for case in test_cases:
    username_test = case[1]
    password_test = case[2]

    print(username_test)
    print(password_test)