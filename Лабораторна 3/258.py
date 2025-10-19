n = int(input())
pi = 0
for i in range(n):
    pi += (-1) ** i * 4 / (2 * i + 1)
print(pi)