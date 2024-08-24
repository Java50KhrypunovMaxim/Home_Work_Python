## Var 1
array = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

new_array_numbers = []
new_array_zero=[]
for i in range(len(array)):
    if array[i] != 0:
        new_array_numbers.append(array[i])
    else:
        new_array_zero.append(array[i])
new_array_numbers.extend(new_array_zero)
print(new_array_numbers)

## Var 2
array2 = [8, 1, 0,0,2]
new_array = []
counter_of_zero = array2.count(0)
for i in range(len(array2)):
    if array2[i] != 0:
        new_array.append(array2[i])
new_array.extend([0] * counter_of_zero)
print(new_array)