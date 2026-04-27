# Задача 1. Поиск фамилий с инициалами в текстовом файле

import re

# Чтение текста из файла
with open("Dostoevsky.txt", encoding="utf-8") as f:
    text = f.read()

print("Исходный текст загружен.")

# Регулярное выражение для поиска инициалов с фамилией
pattern = r"[А-ЯЁ]\.\s?[А-ЯЁ]\.\s?[А-ЯЁ][а-яё]+"

# Поиск всех совпадений
matches = re.findall(pattern, text)

# Удаляем повторы и сортируем
unique_matches = sorted(set(matches))

print("\nНайденные фамилии с инициалами:")
for m in unique_matches:
    print(m)
