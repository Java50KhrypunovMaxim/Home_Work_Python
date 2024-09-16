def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    yield begin
    for i in range(end-1):
        begin = func(begin)
        yield begin

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
gen = some_gen(3, 3, pow)
assert list(gen) == [3, 9, 81], 'Test3'
print('OK')