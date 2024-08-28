
import keyword
import string

reserved_words = keyword.kwlist
punctuation_list = list(string.punctuation)
if "_" in punctuation_list:
    punctuation_list.remove("_")

flag_for_password = True

user_input = input(str("Enter password: "))

if user_input[0].isnumeric():
    flag_for_password = False
    print("Password should not start with a number.")

elif not user_input.islower():
    flag_for_password = False
    print("The password must consist of only lowercase letters and numbers")

elif user_input in reserved_words:
    flag_for_password = False
    print("Password should not be a reserved Python keyword.")

for char in user_input:
    if char in punctuation_list or char == " ":
        flag_for_password = False
        print("Password contains spaces or invalid punctuation.")
        break

print(flag_for_password)
