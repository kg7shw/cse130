value = []

for i in range(10):
    value[i] = int(input(" value: "))

    num_even_odd = [0, 0]

    for num in value:

        assert num % 2 in [0, 1]
        mod = num % 2
        num_even_odd[mod] += 1


print(f"{num_even_odd}")
