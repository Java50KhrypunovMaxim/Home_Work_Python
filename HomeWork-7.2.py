
def correct_sentence(text:str) -> str:
    text = text.strip()
    text = text[0].upper() + text[1:]
    text = list(text)
    if text[len(text)-1] != ".":
           text.append(".")
    text = ''.join(text)
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print('ОК')