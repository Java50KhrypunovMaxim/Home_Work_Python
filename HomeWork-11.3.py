def is_even(number):
    number_like_string = str(number)
    only_numbers = [ int (num) for num in number_like_string ]
    even_numbers = [0,2,4,6,8]
    return only_numbers[len(only_numbers)-1] in even_numbers

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(123)== False, 'Test4'
assert is_even(1)== False, 'Test4'
print("Ok")