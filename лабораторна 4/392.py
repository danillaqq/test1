s = input()
word = ''
max_word = ''
for ch in s:
    if ch.isalpha():
        word += ch
    else:
        if len(word) > len(max_word):
            max_word = word
        word = ''
if len(word) > len(max_word):
    max_word = word
print(max_word)