uppercase_count = 0

# Чтение исходного файла
with open("text18-10.txt", encoding="utf-8") as f:
    lines = f.readlines()

# Подсчёт букв верхнего регистра
for line in lines:
    for ch in line:
        if ch.isupper():
            uppercase_count += 1

# Формируем новый файл
author = "Автор: А.С. Пушкин"
title = "Произведение: К ***"

with open("text18-10_new.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
    f.write("\n" + author + "\n")
    f.write(title + "\n")
