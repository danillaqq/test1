s = input()
num = ''
for ch in s:
    if ch.isdigit():
        num += ch
    elif num:
        print(num, end=', ')
        num = ''
if num:
    print(num)