countries_capitals = {
    'Россия': 'Москва',
    'США': 'Вашингтон',
    'Франция': 'Париж',
    'Германия': 'Берлин',
    'Италия': 'Рим'
}

print("Все страны и их столицы:")
for country, capital in countries_capitals.items():
    print(f"{country}: {capital}")

country = 'Россия'
print(f"\nСтолица страны {country} - {countries_capitals[country]}")

sorted_countries_capitals = sorted(countries_capitals.items())
print("\nОтсортированный список стран и их столиц:")
for country, capital in sorted_countries_capitals:
    print(f"{country}: {capital}")