n = int(input().strip())

words = set()

for _ in range(n):
    line = input().strip()
    for w in line.split():
        words.add(w)

print(len(words))