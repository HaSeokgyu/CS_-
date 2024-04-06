def num_generator(num):
    for n in range(2, num, 2):
        yield n

numbers = num_generator(19)

for num in numbers:
    print(num)