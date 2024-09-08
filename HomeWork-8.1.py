def add_one(some_list):
    some_list_string=''.join(map(str,some_list))
    new_number= int(some_list_string)+1
    result = list(map(int,str(new_number)))
    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")