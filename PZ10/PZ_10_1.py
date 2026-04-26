numbers = [-10, 5, 12, -3, 7, 20, -8, 15]

with open("data_10.txt", "w") as f:
    f.write(" ".join(map(str, numbers)))

# Читаем данные из файла
with open("data_10.txt") as f:
    data = list(map(int, f.read().split()))

# Обработка данных
count_elements = len(data)
reversed_elements = data[::-1]
half_sum = sum(data[len(data)//2:])

# Записываем результаты в новый файл
with open("result_10.txt", "w") as f:
    f.write("Исходные данные:\n")
    f.write(" ".join(map(str, data)) + "\n\n")
    f.write(f"Количество элементов: {count_elements}\n")
    f.write(
        f"Элементы в обратном порядке: {' '.join(map(str, reversed_elements))}\n")
    f.write(f"Сумма элементов последней половины: {half_sum}\n")
