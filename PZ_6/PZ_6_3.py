N = int(input("Введите размер списка N: "))

A = []
for i in range(N):
    A.append(int(input(f"Введите A[{i}]: ")))

print("Исходный список:", A)

for i in range(N - 1, 0, -1):
    A[i] = A[i - 1]
A[0] = 0

print("Список после сдвига вправо:", A)
