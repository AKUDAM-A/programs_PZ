import sqlite3


# Создание таблицы
def create_table():
    try:
        conn = sqlite3.connect("industry.db")
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS enterprises (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                branches INTEGER,
                staff INTEGER,
                equipment_cost REAL,
                production_volume REAL,
                reg_date TEXT
            )
        """)

        conn.commit()
        conn.close()
    except Exception as e:
        print("Ошибка при создании таблицы:", e)


# Добавление записи
def insert_record(data):
    try:
        conn = sqlite3.connect("industry.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO enterprises 
            (id, name, address, branches, staff, equipment_cost, production_volume, reg_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)

        conn.commit()
        conn.close()
    except Exception as e:
        print("Ошибка при добавлении записи:", e)


# Поиск (3 варианта)
def search_by_name(name):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM enterprises WHERE name LIKE ?",
                ('%' + name + '%',))
    result = cur.fetchall()
    conn.close()
    return result


def search_by_staff(min_staff):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM enterprises WHERE staff >= ?", (min_staff,))
    result = cur.fetchall()
    conn.close()
    return result


def search_by_branches(branches):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM enterprises WHERE branches = ?", (branches,))
    result = cur.fetchall()
    conn.close()
    return result


# Удаление (3 варианта)
def delete_by_id(id_):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM enterprises WHERE id = ?", (id_,))
    conn.commit()
    conn.close()


def delete_by_name(name):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM enterprises WHERE name = ?", (name,))
    conn.commit()
    conn.close()


def delete_low_production(limit):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM enterprises WHERE production_volume < ?", (limit,))
    conn.commit()
    conn.close()


# Редактирование (3 варианта)
def update_address(id_, new_address):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("UPDATE enterprises SET address = ? WHERE id = ?",
                (new_address, id_))
    conn.commit()
    conn.close()


def update_staff(id_, new_staff):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute("UPDATE enterprises SET staff = ? WHERE id = ?",
                (new_staff, id_))
    conn.commit()
    conn.close()


def update_equipment_cost(id_, new_cost):
    conn = sqlite3.connect("industry.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE enterprises SET equipment_cost = ? WHERE id = ?", (new_cost, id_))
    conn.commit()
    conn.close()


# Основная часть
create_table()

# Пример добавления 10 записей
sample_data = [
    (1, "Завод А", "Минск, ул. Ленина 10", 3,
     120, 5_000_000, 150_000, "2010-05-12"),
    (2, "Фабрика Б", "Гродно, ул. Советская 5",
     1, 80, 2_300_000, 90_000, "2012-03-20"),
    (3, "Комбинат В", "Брест, ул. Мира 7", 4,
     200, 7_800_000, 300_000, "2008-11-01"),
    (4, "Предприятие Г", "Витебск, ул. Кирова 15",
     2, 150, 4_500_000, 180_000, "2015-09-10"),
    (5, "Завод Д", "Могилёв, ул. Первомайская 3",
     5, 350, 12_000_000, 500_000, "2005-02-18"),
    (6, "Фабрика Е", "Минск, ул. Победы 22",
     1, 60, 1_200_000, 70_000, "2018-07-30"),
    (7, "Комбинат Ж", "Гомель, ул. Лесная 9",
     3, 180, 6_700_000, 250_000, "2011-12-05"),
    (8, "Предприятие З", "Минск, ул. Октябрьская 14",
     2, 140, 3_900_000, 160_000, "2014-06-22"),
    (9, "Завод И", "Брест, ул. Центральная 8",
     4, 220, 8_500_000, 320_000, "2009-04-17"),
    (10, "Фабрика К", "Гродно, ул. Молодёжная 11",
     1, 75, 1_800_000, 95_000, "2016-01-09")
]

for row in sample_data:
    insert_record(row)

print("База данных успешно создана и заполнена.")
