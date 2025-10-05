# Введення даних
a = float(input("Введіть поріг a: "))
b = float(input("Введіть поріг b: "))
c = float(input("Введіть поріг c: "))
s = float(input("Введіть суму s: "))

# Обчислення податку
if s <= a:
    tax = 0
elif s <= b:
    tax = s * 0.10
elif s <= c:
    tax = s * 0.25
else:
    tax = s * 0.50

# Вивід результату
print("Розмір податку:", tax)