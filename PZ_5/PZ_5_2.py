def Minmax(x, y):
    if x > y:
        return y, x
    return x, y


a = float(input("Введите A: "))
b = float(input("Введите B: "))
c = float(input("Введите C: "))
d = float(input("Введите D: "))

a, b = Minmax(a, b)
c, d = Minmax(c, d)
a, c = Minmax(a, c)
b, d = Minmax(b, d)

numbers = [a, b, c, d]

print("Минимальное число:", min(numbers))
print("Максимальное число:", max(numbers))
