N = int(input("Введите размер списка N: "))

A = []
for i in range(N):
    A.append(int(input(f"Введите A[{i}]: ")))

print("Исходный список:", A)

count = 1
i = 2

while i < N:
    if (A[i] - A[i-1]) * (A[i-1] - A[i-2]) < 0:
        count += 1
    i += 1

print("Количество промежутков монотонности:", count)
