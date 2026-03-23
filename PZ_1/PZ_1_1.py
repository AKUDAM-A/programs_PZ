# Формула: Q*6*w + 17*a*x

while True:
    try:
        Q = float(input("Введите значение Q: "))
        break
    except:
        print("Ошибка! Введите число.")

while True:
    try:
        w = float(input("Введите значение w: "))
        break
    except:
        print("Ошибка! Введите число.")

while True:
    try:
        a = float(input("Введите значение a: "))
        break
    except:
        print("Ошибка! Введите число.")

while True:
    try:
        x = float(input("Введите значение x: "))
        break
    except:
        print("Ошибка! Введите число.")

result = Q * 6 * w + 17 * a * x

print("Результат:", result)
print("Программа успешно завершена!")
