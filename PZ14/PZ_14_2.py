import tkinter as tk


def process_numbers():
    raw = entry.get()
    try:
        nums = list(map(int, raw.split()))
    except ValueError:
        result_label.config(text="Ошибка: введите числа через пробел.")
        return

    # Максимальный отрицательный
    negative = [x for x in nums if x < 0]
    max_negative = max(negative) if negative else "нет отрицательных"

    # Чётные элементы
    even = [x for x in nums if x % 2 == 0]
    even_sum = sum(even)

    # Формирование результата
    result = (
        f"Максимальный отрицательный: {max_negative}\n"
        f"Чётные элементы: {even}\n"
        f"Сумма чётных: {even_sum}"
    )
    result_label.config(text=result)


# Окно приложения
root = tk.Tk()
root.title("Обработка чисел")
root.geometry("450x260")

# Поле ввода
tk.Label(root, text="Введите числа через пробел:",
         font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=50, font=("Arial", 11))
entry.pack()

# Кнопка
tk.Button(
    root,
    text="Выполнить",
    command=process_numbers,
    font=("Arial", 12),
    bg="#4d4d4d",
    fg="white"
).pack(pady=10)

# Вывод результата
result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

root.mainloop()
