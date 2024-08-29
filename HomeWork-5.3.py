import string

user_input = input("Enter sentenses: ")
number_of_characters = 140

user_input = user_input.title()

sentenсes_from_user = []

for char in user_input:
    if char not in string.punctuation and char != " ":
        sentenсes_from_user.append(char)

finish_sentenсes = "#" + ''.join(sentenсes_from_user)
if len(finish_sentenсes) > number_of_characters:
    finish_sentenсes = finish_sentenсes [:number_of_characters]

print(finish_sentenсes)
