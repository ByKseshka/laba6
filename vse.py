def zad1():
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

def zad2():
    letter_values = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }

    def calculate_word_value(word):
        value = 0
        for letter in word.upper():
            if letter in letter_values:
                value += letter_values[letter]
        return value

    word = input("Введите слово: ")

    word_value = calculate_word_value(word)

    print(f"Стоимость слова '{word}' равна {word_value} очков.")

def zad3():
students_languages = {
    'Ксения': ['английский', 'французский', 'немецкий'],
    'Анна': ['испанский', 'итальянский'],
    'Мария': ['китайский', 'японский'],
    'Ангелина': ['китайский', 'английский'],
    'Данил': ['французский', 'испанский'],
}

all_languages = set()

for languages in students_languages.values():
    all_languages.update(languages)

print(f"Количество различных языков, которые знают студенты: {len(all_languages)}")
print("Отсортированный список языков:")
for language in sorted(all_languages):
    print(language)

print("\nСтуденты, знающие английский язык:")
for student, languages in students_languages.items():
    if 'английский' in languages:
        print(student)