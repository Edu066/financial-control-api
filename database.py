import sqlite3

def connect_db():
    return sqlite3.connect("finance.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()

