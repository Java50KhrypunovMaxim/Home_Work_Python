def find_unique_value(some_list):
   for number in some_list:
       if some_list.count(number) == 1:
           result = number
           return result
   return None

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
##var2
def find_unique_value2(some_list):
   temp_list = some_list[:]
   for number in temp_list:
       if temp_list.count(number) > 1:
           while number in temp_list:
               temp_list.remove(number)
   if temp_list:
       return temp_list[0]
   return None

assert find_unique_value2([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value2([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value2([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

