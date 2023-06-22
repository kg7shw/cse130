# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-




# Do
#     PROMPT for number
#     GET number
# WHILE number <= 0

# array = [1,2]  Note [1%2] = [1] and [2%2] = [0]

# IF number > 2
#     FOR index = 3 ... number
#         array[index % 2] = array[0] + array[1]

# value = array[number % 2]
# PUT value


number = 0

while number <= 0:
    number = int(input("Which Francois number would you like to see? "))
    assert number > 0 # Number must be greater than 0.

array = [1,2]
assert type(array) == list # array is not a list.

if number > 2:
    for index in range(3, number + 1):
        assert 0 <= index < len(array)  # Index out of range.
        array[index % 2] = array[0] + array[1]
        assert array[index % 2] > array[(index - 1) % 2] # The values in the array are not increasing

value = array[number % 2]
print(value)



