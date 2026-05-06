import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Contact Form")
root.geometry("520x420")
root.configure(bg="#b5b5b5")  # максимально похожий фон

# Заголовок
title = tk.Label(root, text="Contact Form", font=(
    "Arial", 22, "bold"), bg="#b5b5b5")
title.pack(pady=(20, 0))

subtitle = tk.Label(root, text="Please fill all entries.",
                    font=("Arial", 11), bg="#b5b5b5")
subtitle.pack(pady=(0, 15))

# Белая форма
frame = tk.Frame(root, bg="white", bd=1, relief="solid")
frame.pack(padx=20, pady=10, fill="both")

# Левая колонка — подписи
labels_frame = tk.Frame(frame, bg="white")
labels_frame.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="n")

# Правая колонка — поля
fields_frame = tk.Frame(frame, bg="white")
fields_frame.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="n")

# Подписи
label_name = tk.Label(labels_frame, text="Name:",
                      font=("Arial", 11), bg="white")
label_email = tk.Label(labels_frame, text="Email:",
                       font=("Arial", 11), bg="white")
label_message = tk.Label(labels_frame, text="Message:",
                         font=("Arial", 11), bg="white")
label_subject = tk.Label(labels_frame, text="Subject:",
                         font=("Arial", 11), bg="white")

label_name.pack(anchor="w", pady=5)
label_email.pack(anchor="w", pady=5)
label_message.pack(anchor="w", pady=5)
label_subject.pack(anchor="w", pady=5)

# Поля
entry_name = tk.Entry(fields_frame, width=35, font=("Arial", 11))
entry_email = tk.Entry(fields_frame, width=35, font=("Arial", 11))
entry_message = tk.Text(fields_frame, width=35, height=5, font=("Arial", 11))

subject_var = tk.StringVar()
entry_subject = ttk.Combobox(
    fields_frame, textvariable=subject_var, width=33, state="readonly")
entry_subject["values"] = ["Product Inquiry", "Support", "Feedback", "Other"]
entry_subject.current(0)

entry_name.pack(pady=5)
entry_email.pack(pady=5)
entry_message.pack(pady=5)
entry_subject.pack(pady=5)

# Кнопка Send
send_button = tk.Button(
    frame,
    text="Send",
    bg="#4d4d4d",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    height=1
)
send_button.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
