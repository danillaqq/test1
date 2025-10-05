# Введення швидкостей
speed_kmh = float(input("Введіть швидкість у км/год: "))
speed_ms = float(input("Введіть швидкість у м/с: "))

# Переведення км/год у м/с
converted_kmh = speed_kmh * 1000 / 3600

# Порівняння
if converted_kmh > speed_ms:
    result = "швидкість у км/год більша"
elif converted_kmh < speed_ms:
    result = "швидкість у м/с більша"
else:
    result = "швидкості рівні"

# Вивід результату
print(result)