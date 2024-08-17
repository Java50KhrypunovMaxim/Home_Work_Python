number_of_user = int(input("Please enter your number:"))
n1 = number_of_user%10
number_of_user = number_of_user//10
n2 = number_of_user%10
number_of_user = number_of_user//10
n3 = number_of_user%10
number_of_user = number_of_user//10
n4 = number_of_user%10
number_of_user = number_of_user//10
print(n4)
print(n3)
print(n2)
print(n1)
total = int (n1+n2+n3+n4)
print(f"The sum of all the digits in a number = {total} ")