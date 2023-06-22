user_num = int(input("Which François number in the sequence would you like to compute? "))

seq_index = user_num - 1


f1 = int(input("Give me f1: "))
f2 = int(input("Give me f2: "))

seq_list = [f1, f2]
check_num_1 = f1
check_num_2 = f2

for i in range(seq_index - 1):
    new_num = check_num_1 + check_num_2
    seq_list.append(new_num)
    check_num_1, check_num_2 = check_num_2, new_num

print(seq_list[seq_index])
print(seq_list)
print(seq_list[4])
