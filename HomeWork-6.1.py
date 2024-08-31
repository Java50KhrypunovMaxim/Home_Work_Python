# Variant 1
import string

user_input = input("Enter letter range: ").strip()
string_input = list(user_input)
start_symbol =  ord(string_input[0])
finish_symbol = ord(string_input[2])
result = []
if start_symbol<=finish_symbol:
    for a in range(start_symbol,finish_symbol+1):
        result.append(chr(a))
else:
    for i in range(start_symbol, ord('z') + 1):
        result.append(chr(i))
    for i in range(ord('A'), finish_symbol + 1):
        result.append(chr(i))
result_string = ''.join(result)
print(result_string)

# Variant 2
user_input_2 = input("Enter letter range: ").strip()
all_symbols = string.ascii_letters
string_input2 = list(user_input_2)
start_index =  all_symbols.index(string_input2[0])
finish_symbol = all_symbols.index(string_input2[2])
result2 = (all_symbols[start_index:finish_symbol+1])
print(result2)