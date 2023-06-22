num = int(input("Which François number in the sequence would you like to compute? "))

lookup = {}


def francois(num):
    if num == 1:
        result = 2
        return result
    elif num == 2:
        result = 1
        return result
    else:
        result = francois(num - 1) + francois(num - 2)
        return result
    
    lookup




first_num = 2
second_num = 1

sequence_list = []

sequence_list.append(first_num, second_num)
check_num_1 = first_num
check_num_2 = second_num

for i in sequence_list:

    new_num = check_num_1 + check_num_2
    sequence_list.append(new_num)
    check_num_1 = check_num_2
    check_num_2 = new_num


# Got it, Used it, used it then never used it again
