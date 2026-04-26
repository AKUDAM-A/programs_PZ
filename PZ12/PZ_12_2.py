matrix = [
    [4, -2, 7, 1],
    [9, 3, -5, 8],
    [10, 20, 30, 40],
    [5, 11, -1, 3]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

# Список всех положительных элементов
positive = [x for row in matrix for x in row if x > 0]

# Среднее арифметическое
avg = sum(positive) / len(positive) if positive else 0

print("\nПоложительные элементы:", positive)
print("Среднее арифметическое положительных элементов:", avg)
