# user_num = int(input("Which François number in the sequence would you like to compute? "))

# seq_index = user_num - 1


# f1 = int(input("Give me f1: "))
# f2 = int(input("Give me f2: "))

# seq_list = [f1, f2]
# check_num_1 = f1
# check_num_2 = f2

# for i in range(seq_index - 1):
#     new_num = check_num_1 + check_num_2
#     seq_list.append(new_num)
#     check_num_1, check_num_2 = check_num_2, new_num

# print(seq_list[seq_index])
# print(seq_list)
# print(seq_list[4])



import time
import matplotlib.pyplot as plt

# Function to compute the nth number in the sequence
def compute_nth_number(n, f1, f2):
    seq_list = [f1, f2]
    check_num_1 = f1
    check_num_2 = f2

    for i in range(n - 2):
        new_num = check_num_1 + check_num_2
        seq_list.append(new_num)
        check_num_1, check_num_2 = check_num_2, new_num

    return seq_list[n - 1]

# List of values of n to test
n_values = [10, 20, 30, 40, 50]

# List to store the time taken for each value of n
time_taken = []

# Test and measure the time for each value of n
for n in n_values:
    start_time = time.time()
    compute_nth_number(n, 0, 1)
    end_time = time.time()
    time_taken.append(end_time - start_time)

# Plotting the results
plt.plot(n_values, time_taken, marker='o')
plt.xlabel('n')
plt.ylabel('Time taken (seconds)')
plt.title('Efficiency of Computing the nth Number in the Sequence')
plt.show()

