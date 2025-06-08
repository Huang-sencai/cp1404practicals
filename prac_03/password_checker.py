MAX_LENGTH = 15
MIN_LENGTH = 5
SPECIAL_CHARACTERS = " !@#$%^&*()_-=+`~,./'[]<>?{}|\\"
lower = 0
upper = 0
digit = 0
special = 0
wrong=0
print("Please enter a valid password")
print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
print("    1 or more uppercase characters")
print("    1 or more lowercase characters")
print("    1 or more numbers")
print(f"    and 1 or more special characters:  {SPECIAL_CHARACTERS}")
password = str(input("> "))
if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        wrong+=1
for char in password:
    if char.islower():
        lower += 1
    elif char.isupper():
        upper += 1
    elif char.isdigit():
        digit += 1
    elif char in SPECIAL_CHARACTERS:
        special += 1
if lower == 0 or upper == 0 or digit == 0 or special==0:
    wrong+=1
    while wrong>0:
        print("Invalid password!")
        password = str(input("> "))
        lower = 0
        upper = 0
        digit = 0
        special = 0
        wrong = 0
        if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
            wrong += 1
        for char in password:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                digit += 1
            elif char in SPECIAL_CHARACTERS:
                special += 1
        if lower == 0 or upper == 0 or digit == 0 or special == 0:
            wrong += 1
print(f"Your {len(password)} character password is valid: {password}")