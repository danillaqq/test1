def get_bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "equal"

# Зчитуємо три рядки по два числа
pairs = []
for _ in range(3):
    a, b = map(int, input().split())
    print(get_bigger(a, b))