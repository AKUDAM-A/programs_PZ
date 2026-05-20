import sqlite3


def init_db():
    conn = sqlite3.connect("court_cases.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_number TEXT,
            decision_date TEXT,
            location TEXT,
            judge TEXT,
            plaintiff TEXT,
            defendant TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_to_db(parsed_data):
    conn = sqlite3.connect("court_cases.db")
    cursor = conn.cursor()
    for record in parsed_data:
        cursor.execute("""
            INSERT INTO cases (case_number, decision_date, location, judge, plaintiff, defendant)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            record.get("case_number"),
            record.get("decision_date"),
            record.get("location"),
            record.get("judge"),
            record.get("plaintiff"),
            record.get("defendant")
        ))
    conn.commit()
    conn.close()
