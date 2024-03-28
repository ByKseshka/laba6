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