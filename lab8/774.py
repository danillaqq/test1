import re
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.com'
result = re.findall(pattern, text)
print(result)