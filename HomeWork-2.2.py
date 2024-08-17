start_number = int(input("Please enter your number:"))
num1 = start_number%10 * 10**4
start_number = start_number//10
num2 = start_number%10 * 10**3
start_number = start_number//10
num3 = start_number%10 * 10**2
start_number = start_number//10
num4 = start_number%10 * 10
start_number = start_number//10
num5 = start_number%10
return_number = int (num5+num4+num3+num2+num1)
print(f"Return number - {return_number} ")