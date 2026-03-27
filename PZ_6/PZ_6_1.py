# Ввод размера списка
N = int(input("Введите размер списка N (>2): "))

# Ввод списка
A = []
for i in range(N):
    A.append(int(input(f"Введите элемент A[{i}]: ")))

K = int(input("Введите число K (1 < K < N): "))

print("Исходный список:", A)

# Вывод элементов с номерами, кратными K
print("Элементы с номерами, кратными K:")
index = K - 1
while index < N:
    print(A[index], end=' ')
    index += K
