movies = {
    "Avengers: Endgame": 2019,
    "Guardians of the Galaxy": 2014,
    "Iron Man": 2008,
    "Thor": 2011
}

# Сортування за ключами (назвами фільмів)
for title, year in sorted(movies.items()):
    print(f"('{title}', {year})", end=" ")