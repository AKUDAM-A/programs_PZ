def Minmax(x, y):
    if x > y:
        return y, x
    return x, y

# ввод с проверкой


def read_number(text):
    n = input(text)
    while True:
        try:
            n = float(n)
            return n
        except ValueError:
            print("Неправильно ввели!")
            n = input(text)


a = read_number("Введите A: ")
b = read_number("Введите B: ")
c = read_number("Введите C: ")
d = read_number("Введите D: ")

# четыре вызова функции, как требует задание
a, b = Minmax(a, b)
c, d = Minmax(c, d)
a, c = Minmax(a, c)
b, d = Minmax(b, d)

# корректный поиск минимума и максимума
numbers = [a, b, c, d]

print("Минимальное число:", min(numbers))
print("Максимальное число:", max(numbers))
