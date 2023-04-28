# 1. Name: 
#    Grant Call
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    a program in Python to display a message on the screen, prompt the user for information, make a decision, store data in a list, and loop. 
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of the assignment was remembering the python syntax. It has been a while since I have written in python so it was a challenge to remember. It was also difficult to think though the while loop and what was needed for it. The last part was figueing out the length of the array. I had to look up documentation in w3schools
# 5. How long did it take for you to complete the assignment?
#    2 hours  



# Game introduction.
# Prompt the user for how difficult the game will be. Ask for an integer.
# Generate a random number between 1 and the chosen value.
# Give the user instructions as to what he or she will be doing.
# Initialize the sentinal and the array of guesses.
# Play the guessing game.
    # Prompt the user for a number.
    # Store the number in an array so it can be displayed later.
    # Make a decision: was the guess too high, too low, or just right.
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