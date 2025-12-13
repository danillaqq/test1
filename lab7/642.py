def sort_words(sequence: str) -> str:
    words = sequence.split('-')
    words.sort()
    return '-'.join(words)
input_data = input("Введіть слова, розділені дефісами: ")
result = sort_words(input_data)
print(result)