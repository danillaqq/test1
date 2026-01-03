import re
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
result = set(emails)
print(result)