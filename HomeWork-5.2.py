flag_for_finish = True
while flag_for_finish:
    number_1 = int(input("Please enter your first  number:"))
    operation = str(input("Please indicate the mathematical operation:\n"
                          "1) Addition (+)\n"
                          "2) Subtraction (-)\n"
                          "3) Multiplication (*)\n"
                          "4) Division (/)\n"))
    number_2 = int(input("Please enter your second  number:"))
    match operation:
        case "+":
            result = number_1 + number_2
            print(f"Result = {result}")
        case "-":
            result = number_1 - number_2
            print(f"Result = {result}")
        case "*":
            result = number_1 * number_2
            print(f"Result = {result}")
        case "/":
            if number_2 == 0:
                print("Error. You can't divide by zero.")
            else:
                result = number_1 / number_2
                print(f"Result = {result}")
        case _:
            print("Invalid operation selected.")
    quest = input("Do you want to continue working with the calculator? (Yes - Y, No - N or another word): ")
    if quest.lower() != "y":
        flag_for_finish = False
        print("Thank you for completing your work.")