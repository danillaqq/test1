# Введення числа
number = int(input("Введіть двоцифрове число: "))

# Витягування цифр
digit1 = number // 10
digit2 = number % 10

# Обчислення суми
digit_sum = digit1 + digit2

# Перевірка, чи сума є двоцифровим числом
is_two_digit = digit_sum >= 10

# Вивід результату
print(is_two_digit)
