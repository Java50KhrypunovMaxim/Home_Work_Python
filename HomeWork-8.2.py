import string
from sys import flags

def is_palindrome(text):
    flag = True
    text = text.strip().lower()
    text = text.replace(' ', '')
    for symbol in string.punctuation:
        text = text.replace(symbol,'')
    text = list(text)
    i=0
    j=len(text)-1
    while i < j:
        if text[i] != text[j]:
            flag = False
            break
        i+=1
        j-=1
    return flag

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

##var 2
def is_palindrome2(text):
    text = text.strip().lower()
    text = ''.join(char for char in text if char.isalnum())
    return text == text[::-1]

assert is_palindrome2('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome2('0P') == False, 'Test2'
assert is_palindrome2('a.') == True, 'Test3'
assert is_palindrome2('aurora') == False, 'Test4'
print("ОК")