# 1. Name: 
#    Grant Call
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#    -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  

import random

# Game introduction.
print()
print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.')
print()
# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input('Pick a positive integer: '))
# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.

# Initialize the sentinal and the array of guesses.
array = []

guess_num = int(input(f'Guess a number between 1 and {value_max}. '))
array.append(guess_num)
print()
# Play the guessing game.

    # Prompt the user for a number.

    # Store the number in an array so it can be displayed later.

    # Make a decision: was the guess too high, too low, or just right.
if guess_num > value_random:
    print('Too high!')
elif guess_num < value_random:
    print('Too low!')
else:
    print('You were able to find the number in {num_of_guesses} guesses.')
    print(f'The numbers you guessed were: {array}')

# Give the user a report: How many guesses and what the guesses where.


import random
print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.\n')

value_max = int(input('Pick a positive integer: '))
value_random = random.randint(1, value_max)
guess_num = print(f'Guess a number between 1 and {value_max}. ')
array = []

while guess_num != value_random:
    guess_num = int(input('> '))
    array.append(guess_num)
    if guess_num > value_random:
        print('\tToo high!')
    
    elif guess_num < value_random:
        print('\tToo low!')

print(f'You were able to find the number in {len(array)} guesses.')
print(f'The numbers you guessed were: {array}')
