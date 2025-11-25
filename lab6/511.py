# Початковий словник
countries = {
    'Ukraine': 'Kyiv',
    'France': 'Paris',
    'Denmark': 'Copenhagen',
    'China': 'Beijing',
    'Canada': 'Ottawa'
}

# Сортування за спаданням ключів (назв країн)
sorted_items = sorted(countries.items(), reverse=True)

# Вивід результату
print(sorted_items)