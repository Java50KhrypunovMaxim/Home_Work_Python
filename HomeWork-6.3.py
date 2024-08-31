user_input = (input("Enter the number: "))

if not user_input.isdigit():
    print("Input must be a number.")
else:
    digits = list(user_input)
    const_number = 9

    while True:
        result = 1
        for i in range (len(digits)):
            result *= int(digits[i])
        if result <= const_number:
            break
        digits = list(str(result))

    print(result)