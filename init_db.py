import sqlite3

connection = sqlite3.connect("assignments.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    course TEXT NOT NULL,
    due_date TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0
)
""")

connection.commit()
connection.close()

print("Database initialized.")
