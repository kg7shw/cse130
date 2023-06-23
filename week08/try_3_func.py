def get_françois_num():
    while not done:
        françois_number = int(input("Enter a number: "))
        if françois_number > 0:
            done = True
        else:
            print("Invalid input. Please input a number greater than 0.")
    return françois_number


def calculate_françois_num(françois_number):
    array = [1, 2]
    if françois_number > 2:
        for index in range(3, françois_number + 1):
            array[index % 2] = array[0] + array[1]

    value = array[françois_number % 2]
    return value

def run_test_cases():
    test_cases = [-1, 0, 1, 2, 9, 100, 200]
    for françois_number in test_cases:
        if françois_number > 0:
            print(f"Francois number for case {françois_number}: {calculate_françois_num(françois_number)}")
        else:
            print(f"Case {françois_number}: The input was less than zero")
        

def main():
    choice = input("Do you want to run the test cases? (y/n): ")
    if choice == "y":
        run_test_cases()
    else:
        françois_number = get_françois_num()
        value = calculate_françois_num(françois_number)
        print(f"Result: {value}")


if __name__ == '__main__':
    main()