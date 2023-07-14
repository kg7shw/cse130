import math

def get_range():
    n_range = int(input("Enter the range number: "))
    # print(n_range)
    return n_range

def get_bool_array(n_range):
    is_prime_array = [True] * (n_range + 1)
    is_prime_array[0] = False
    is_prime_array[1] = False
    # print(is_prime_array)
    return is_prime_array

def compute_sqrt(n_range):
    square_n = int(math.sqrt(n_range))
    # print(square_n)
    return square_n

def compute_prime_numbers(n_range, square_n, is_prime_array):
    for current_index in range(2, square_n + 1):
        if is_prime_array[current_index]:
            for i_multiple in range(current_index * 2, n_range + 1, current_index):
                is_prime_array[i_multiple] = False
    # print(is_prime_array)
    return is_prime_array

def get_prime_numbers_array(n_range, is_prime_array):
    prime_nums = []
    for num_index in range(n_range + 1):
        if is_prime_array[num_index]:
            prime_nums.append(num_index)
    # print(prime_nums)
    return prime_nums

def auto_test():
    test_values = [-1, 0, 1, 2, 10, 53, 100, 200]


    count = 0
    for value in test_values:
        count += 1
        print("=========================================================================================")
        print(f"Test case: #{count} - Testing input value {value}\n")
        if value >= 2:
            n_range = value
            original_is_prime_array = get_bool_array(n_range)
            square_n = compute_sqrt(n_range)
            new_is_prime_array = compute_prime_numbers(n_range, square_n, original_is_prime_array)
            prime_nums = get_prime_numbers_array(n_range, new_is_prime_array)
            print(f"This program will find all the prime numbers at or below N. Select that N: {n_range}")
            print(f"The prime numbers at or below {value} are {prime_nums}")
            print("=========================================================================================\n")
        else:
            print(f"Value: {value} is less than 2 and therfore not a prime number")
        




def main():
    auto_test()
    n_range = get_range()
    original_is_prime_array = get_bool_array(n_range)
    square_n = compute_sqrt(n_range)
    new_is_prime_array = compute_prime_numbers(n_range, square_n, original_is_prime_array)
    prime_nums = get_prime_numbers_array(n_range, new_is_prime_array)

    print(prime_nums)

if __name__ == "__main__":
    main()
