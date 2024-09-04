name_user = "Anton     "
age_user=120

def say_hi(name:str,  age:int) -> str:
    name = name.strip()
    if name.isalpha() and isinstance(age, int) and (0 < age <= 120):
        text = f"Hi. My name is {name} and I'm {age} years old"
    else:
        text=("Data entry error. Age - must be only a number from 0 until 120. "
              "Name must consist of letters only.")
    return text

print(say_hi(name_user, age_user))
result = say_hi(name_user, age_user) == "Hi. My name is Anton and I'm 120 years old"
print(result)

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')