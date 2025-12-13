def is_anagram(a, b):
    return sorted(a.replace(" ", "")) == sorted(b.replace(" ", ""))
s1 = input("Введіть перший рядок: ")
s2 = input("Введіть другий рядок: ")
print(is_anagram(s1, s2))