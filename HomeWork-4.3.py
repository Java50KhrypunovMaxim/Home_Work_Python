import random

random_array = []
finish_array = []
for i in range(random.randint(3, 10)):
    random_array.append(random.randint(1, 100))
print(random_array)
finish_array.append(random_array[0])
finish_array.append(random_array[2])
finish_array.append(random_array[-2])
print(finish_array)