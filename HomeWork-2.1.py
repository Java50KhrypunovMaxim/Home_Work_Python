number = int(input("Please enter your number:"))
n1 = number%10
number = number//10
n2 = number%10
number = number//10
n3 = number%10
number = number//10
n4 = number%10
number = number//10
print(n4)
print(n3)
print(n2)
print(n1)
total = int (n1+n2+n3+n4)
print(f"The sum of all the digits in a number = {total} ")