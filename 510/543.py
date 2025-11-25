# Введення рядка користувачем
text = input()

# Розбиваємо рядок на слова
words = text.split()

# Підрахунок частоти слів
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# Сортування у зворотному буквенному-цифровому порядку
sorted_words = sorted(freq.items(), reverse=True)

# Виведення результату
for word, count in sorted_words:
    print(f"{word}: {count}")