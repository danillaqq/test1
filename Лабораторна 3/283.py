prev = int(input())
count = 0

while True:
    curr = int(input())
    if curr == 0:
        break
    if prev > curr:
        count += 1
    prev = curr

print(count)