# # Print hello world on the screen.
# print("\n\nHello World. \n\n")

# # num = 130
# # print(f"This is CSE {num}.")
# # class_num = 130
# # print("This is CSE " + str(class_num))


# # num_list = [2,4,6]
# # print(num_list)
# # data = [2,4,6]
# # for datum in data:
# #     print(datum)


# # age = int(input('Enter your age: '))
# # age = float(input('Enter your age: '))


# start = int(input("Where do you want to start? "))
# end = int(input("Where do you want to end? "))
# step = int(input("What do you want to count by? "))
# for value in range(start, end +1, step):
#     print(value)




# counter = start
# while counter <= end:
#     print(counter)
#     counter += step

# #avoid spegetti code
# # pass, contiue, go to, quit, end, etc













# for i in range(10):
#     print(i)










# prompt = input("keep going? ")

# while prompt != "stop":
#     prompt = input("keep going? ")
# print('finished')


response = "go"
while response != "stop":
    response = input("keep going? ")
print('finished')


#recursion


gender = input('what is your gender? ')

if gender == "male" or gender == "Male":
    is_male = True
else:
    gender = False

print(f"Male is {is_male}")


gender = input('what is you male?(y/n): ')
is_male = True if gender == "y" else False







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
print()
print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.')
print()

value_max = int(input('Pick a positive integer: '))
value_random = random.randint(1, value_max)
guess_num = print(f'Guess a number between 1 and {value_max}. ')
array = []

while value_max != value_random:
    guess_num = int(input('> '))
    array.append(guess_num)
    if guess_num > value_random:
        print('Too high!')
    
    elif guess_num < value_random:
        print('Too low!')

print('You were able to find the number in {num_of_guesses} guesses.')
print(f'The numbers you guessed were: {array}')







