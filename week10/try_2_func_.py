done = False
while not done:

    number = int(input("Enter a number: "))
    if number > 0:
        done = True
    else:
        print("Invalid input. Please input a number greater than 0.")

array = [1, 2]

if number > 2:
    for index in range(3, number + 1):
        array[index % 2] = array[0] + array[1]

value = array[number % 2]
print(f"Result: {value}")


