# Введення типу кімнати
room_type = input("Введіть тип кімнати (triangle, rectangle, circle): ")

# Обчислення площі залежно від типу
if room_type == "triangle":
    a = float(input("Введіть сторону a: "))
    h = float(input("Введіть висоту h: "))
    area = 0.5 * a * h

elif room_type == "rectangle":
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    area = a * b

elif room_type == "circle":
    r = float(input("Введіть радіус r: "))
    area = 3.14 * r * r

else:
    area = "Невідомий тип кімнати"

# Вивід результату
print("Площа кімнати:", area)