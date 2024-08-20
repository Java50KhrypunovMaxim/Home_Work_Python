start_array = [1,2,3]
if len(start_array)==0:
    first_array = []
    second_array = []
    result = [first_array, second_array]
    print(result)
elif len(start_array)%2==0:
    first_array = start_array[:len(start_array)//2]
    second_array = start_array[len(start_array)//2:]
    result = [first_array, second_array]
    print(result)
else:
    first_array = start_array[:len(start_array)//2+1]
    second_array = start_array[len(start_array)//2+1:]
    result = [first_array, second_array]
    print(result)