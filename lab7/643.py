def remove_chars(text, chars_to_remove):
    result = ""
    for ch in text:
        if ch not in chars_to_remove:
            result += ch
    return result
initial = input()
remove_set = input()
output = remove_chars(initial, remove_set)

print(output)