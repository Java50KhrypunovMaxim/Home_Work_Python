#var 1
def common_elements():
    array_multiple_5 = {i for i in range(100) if i % 5 == 0}
    array_multiple_3 = {i for i in range(100) if i % 3 == 0}
    array_result =array_multiple_5 & array_multiple_3
    return array_result
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")

def common_elements2():
        set_multiple_5 = set()
        for i in range(100):
            if i % 5 == 0:
                set_multiple_5.add(i)
        set_multiple_3 = set()
        for i in range(100):
            if i % 3 == 0:
                set_multiple_3.add(i)
        result = set_multiple_5.intersection(set_multiple_3)
        return result
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
