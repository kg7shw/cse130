# import math

# def findPrimes(n):
#     isPrime = [True] * (n + 1)
#     isPrime[0] = isPrime[1] = False

#     for i in range(2, int(math.sqrt(n)) + 1):
#         if isPrime[i]:
#             for j in range(i * i, n + 1, i):
#                 isPrime[j] = False

#     primes = []
#     for i in range(2, n + 1):
#         if isPrime[i]:
#             primes.append(i)

#     return primes

# # Prompt the user for input
# n = int(input("Enter a number: "))

# # Compute and display the prime numbers
# primes = findPrimes(n)
# print("Prime numbers at or below", n, "are:", primes)


import math

def findPrimes(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for currentNum in range(2, int(math.sqrt(n)) + 1):
        if isPrime[currentNum]:
            for multiple in range(currentNum * currentNum, n + 1, currentNum):
                isPrime[multiple] = False

    primes = []
    for number in range(2, n + 1):
        if isPrime[number]:
            primes.append(number)

    return primes


# Prompt the user for input
n = int(input("Enter a number: "))

# Compute and display the prime numbers
primes = findPrimes(n)
print("Prime numbers at or below", n, "are:", primes)

