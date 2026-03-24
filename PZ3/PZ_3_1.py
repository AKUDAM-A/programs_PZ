# Даны два целых числа: A, B.
# Проверить истинность высказывания:
# «Ровно одно из чисел A и B нечетное».

while True:
    try:
        a = int(input("Введите целое число A: "))
        break
    except ValueError:
        print("Ошибка! Повторите ввод A.")

while True:
    try:
        b = int(input("Введите целое число B: "))
        break
    except ValueError:
        print("Ошибка! Повторите ввод B.")

result = (a % 2 != 0 and not b % 2 != 0) or (not a % 2 != 0 and b % 2 != 0)

print("Ровно одно из чисел A и B нечетное:", result)
