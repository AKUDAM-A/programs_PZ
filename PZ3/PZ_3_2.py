# Определить количество дней в этом месяце для невисокосного года.

while True:
    try:
        month = int(input("Введите номер месяца (1-12): "))
        break
    except ValueError:
        print("Неправильно ввели! Повторите ввод.")


if month == 2:
    days = 28
    print("Количество дней в месяце:", days)
elif month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
    print("Количество дней в месяце:", days)
elif month in (4, 6, 9, 11):
    days = 30
    print("Количество дней в месяце:", days)
else:
    print("Ошибка: месяца с таким номером не существует.")
