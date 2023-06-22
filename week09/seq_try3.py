user_num = int(input("Which François number in the sequence would you like to compute? "))
assert user_num == int

f1 = int(input("Give me f1: "))
f2 = int(input("Give me f2: "))
assert f1 == int
assert f1 == int

seq_list = [f1, f2]
assert seq_list == []
seq_index = user_num - 1
assert seq_index is not None
check_num_1 = f1
check_num_2 = f2

for i in range(seq_index - 1):
    assert 0 <= i < len(seq_list)  # Index out of range.

    new_num = check_num_1 + check_num_2
    seq_list.append(new_num)
    check_num_1, check_num_2 = check_num_2, new_num

print(seq_list[seq_index])
print(seq_list)
