# Задане число днів
days = 15

# Обчислення тривалості
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Виведення з форматуванням ширини 10 знаків
print(f"{hours:<10}hours")
print(f"{minutes:<10}minutes")
print(f"{seconds:<10}seconds.")
