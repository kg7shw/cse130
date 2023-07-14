# import math

# def get_prime_numbers(n_range):
#     is_prime_array = [True] * n_range
#     is_prime_array[0] = False

#     for current_index in range(2, int(math.sqrt(n_range)) + 1):
#         if is_prime_array[current_index - 1]:
#             for i_multiple in range(current_index * 2, n_range + 1, current_index):
#                 is_prime_array[i_multiple - 1] = False

#     prime_nums = [num_index + 1 for num_index, is_prime in enumerate(is_prime_array) if is_prime]

#     assert len(prime_nums) >= 2  # The amount of prime numbers should be greater than or equal to 2.
#     assert prime_nums[0] == 2  # The first prime number should be 2.
#     assert prime_nums[-1] <= n_range  # The last prime number should be less than or equal to n_range.

#     for index in range(len(prime_nums) - 1):
#         assert prime_nums[index] < prime_nums[index + 1]  # Prime numbers are increasing.

#     return prime_nums

# n_range = int(input("Enter the range: "))
# prime_nums = get_prime_numbers(n_range)
# print(prime_nums)



import math

n_range = 0
while n_range < 2:
    n_range = int(input("Enter a number greater than or equal to 2: "))

is_prime_array = [True] * (n_range + 1)
is_prime_array[0] = False
is_prime_array[1] = False

square_n = int(math.sqrt(n_range))

for current_index in range(2, square_n + 1):
    if is_prime_array[current_index]:
        for i_multiple in range(current_index * 2, n_range + 1, current_index):
            is_prime_array[i_multiple] = False

prime_nums = []
for num_index in range(n_range + 1):
    if is_prime_array[num_index]:
        prime_nums.append(num_index)

assert len(prime_nums) > 0
assert prime_nums[0] == 2
assert prime_nums[-1] <= n_range

for index in range(1, len(prime_nums)):
    assert prime_nums[index - 1] < prime_nums[index]

print(prime_nums)

