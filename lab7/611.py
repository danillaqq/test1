def get_first_n_chars(n, s):
    return s if len(s) < n else s[:n]

# Читаємо перший набір даних
n1 = int(input())
s1 = input()

# Читаємо другий набір даних
n2 = int(input())
s2 = input()

# Виводимо результати
print(get_first_n_chars(n1, s1))
print(get_first_n_chars(n2, s2))