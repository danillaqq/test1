n = input()  # зчитуємо число як рядок

# знаходимо максимальну і мінімальну цифри
max_digit = int(max(n))
min_digit = int(min(n))

# перевіряємо, чи різниця парна
diff = max_digit - min_digit
print(diff % 2 == 0)