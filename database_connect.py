import sqlite3 as sql

def data_write(name, height, weight, hipc, waistc, bmi, bai, whr):
    print("\nConnecting to database...")
    conn = sql.connect('storage.db')

    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS storage (
        id INTEGER PRIMARY KEY,
        user TEXT,
        height REAL,
        weight REAL,
        hipc REAL,
        waistc REAL,
        bmi REAL,
        bai REAL,
        whr REAL,
        created_at TEXT
    )
    """)

    conn.commit()
    print("Database connected...")

    c.execute(
        "INSERT INTO storage (user, height, weight, hipc, waistc, bmi, bai, whr) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (name, height, weight, hipc, waistc, bmi, bai, whr)
        )

    conn.commit()
    print("Completed writing to database successfully!")
    conn.close()

def data_receive():
    print("Connecting to database...")
    conn = sql.connect('database.db')
    c = conn.cursor()


