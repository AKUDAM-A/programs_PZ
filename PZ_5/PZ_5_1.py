def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def steps_to_zero(n):
    step_count = 0
    while n > 0:
        n -= sum_digits(n)
        step_count += 1
    return step_count


# корректный ввод
while True:
    n = input("Введите целое число (>0): ")
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Неправильно ввели! Введите положительное целое число.")


print("Количество действий до нуля:", steps_to_zero(n))
