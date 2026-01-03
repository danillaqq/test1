import re

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{8,12}$'

while True:
    try:
        password = input()
        if re.match(pattern, password):
            print("Valid")
        else:
            print("Invalid")
    except EOFError:
        break