

array = [0, 1, 7, 2, 4, 8]
sum_of_numbers = 0
for i in range(0,len(array),2):
    sum_of_numbers += array[i]
if len(array) != 0:
    res = sum_of_numbers * array[-1]
else:
    res = sum_of_numbers
print(res)
