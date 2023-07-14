import math

def get_range():
    n_range = 0
    while n_range < 2:
        n_range = int(input("Enter the range number: "))
        if n_range >= 2:
            return n_range
        else:
            print(f"Input number {n_range} is less than 2. Input a number that is equal to or greater than 2")

def get_bool_array(n_range):
    is_prime_array = [True] * (n_range + 1)
    is_prime_array[0] = False
    is_prime_array[1] = False
    return is_prime_array

def compute_sqrt(n_range):
    square_n = int(math.sqrt(n_range))
    return square_n

def compute_prime_numbers(n_range, square_n, is_prime_array):
    for current_index in range(2, square_n + 1):
        assert 2 <= current_index <= square_n + 1 # current_index is out of range
        if is_prime_array[current_index]:
            for i_multiple in range(current_index * 2, n_range + 1, current_index):
                assert current_index <= i_multiple <= square_n + 1 # i_multiple is out of range
                is_prime_array[i_multiple] = False
    return is_prime_array

def get_prime_numbers_array(n_range, is_prime_array):
    prime_nums = []
    for num_index in range(n_range + 1):
        assert 0 <= num_index <= n_range + 1 # num_index is out of range
        if is_prime_array[num_index]:
            prime_nums.append(num_index)
    return prime_nums

def auto_test():
    test_values = [-1, 0, 1, 2, 10, 53, 100, 200]
    assert type(test_values) == list

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
    assert type(n_range) == int # n_range is not an integer
    original_is_prime_array = get_bool_array(n_range)
    assert type(original_is_prime_array) == list # original_is_prime_array is not a list
    square_n = compute_sqrt(n_range)
    assert type(square_n) == int # square_n is not an integer
    new_is_prime_array = compute_prime_numbers(n_range, square_n, original_is_prime_array)
    assert type(new_is_prime_array) == list # new_is_prime_array is not a list
    prime_nums = get_prime_numbers_array(n_range, new_is_prime_array)
    assert type(prime_nums) == list # prime_nums is not a list

    print(prime_nums)

if __name__ == "__main__":
    main()
