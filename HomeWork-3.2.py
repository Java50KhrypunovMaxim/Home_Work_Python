start_array = [1,2,3,5]
if len(start_array)==0:
    print(start_array)
else:
    start_array.insert(0, start_array[-1])
    finish_array = start_array[:-1]
    print(finish_array)