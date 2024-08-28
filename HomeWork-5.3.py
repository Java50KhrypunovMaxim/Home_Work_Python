import string

user_input = input(str("Enter sentenses: "))

user_input = user_input.title()

sentenсes_from_user = []

for char in user_input:
    if char not in string.punctuation and char != " ":
        sentenсes_from_user.append(char)

finish_sentenсes = "#" + ''.join(sentenсes_from_user)
if len(finish_sentenсes) > 140:
    finish_sentenсes = finish_sentenсes [:140]

print(finish_sentenсes)
