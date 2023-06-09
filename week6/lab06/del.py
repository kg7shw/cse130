def create_test_lists():
    num_lists = int(input("How many lists do you want? "))

    lists = []
    for i in range(num_lists):
        length = int(input(f"Enter the length of list {i+1}: "))
        new_list = list(range(1, length + 1))
        lists.append(new_list)

    return lists


test_lists = create_test_lists()
print(test_lists)