total = 0

while True:
    line = input().strip()
    if line == "":      # порожній рядок — завершення
        break

    op, amount = line.split()
    amount = int(amount)

    if op == "D":
        total += amount
    elif op == "W":
        total -= amount

print(total)