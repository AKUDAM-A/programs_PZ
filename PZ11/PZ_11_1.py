numbers = [-12, 5, -3, 8, 14, -7, 20, -1, 6]

print("Исходная последовательность:", numbers)

# 1. Максимальный среди отрицательных
negative = [x for x in numbers if x < 0]
max_negative = max(negative) if negative else None

# 2. Элементы, кратные двум
even_elements = [x for x in numbers if x % 2 == 0]

# 3. Сумма элементов, кратных двум
even_sum = sum(even_elements)

print("Максимальный среди отрицательных:", max_negative)
print("Элементы, кратные двум:", even_elements)
print("Сумма элементов, кратных двум:", even_sum)
