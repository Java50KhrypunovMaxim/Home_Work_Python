def sum_of_digits(number):
    str_number = str(number)
    if str_number[0] == '-':
        str_number = str_number[1:]
    res = sum(int(digit) for digit in str_number)
    return res

def find_gcd(a, b):
    res_array = []
    for i in range(1,100):
        if a%i == 0 and b%i == 0:
            res_array.append(i)
    return max(res_array)

print(find_gcd(15,45))