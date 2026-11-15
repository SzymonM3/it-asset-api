from pathlib import Path
import sqlite3


DATABASE_PATH = Path(__file__).resolve().parent / "data" / "assets.db"


def get_connection():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def init_db():
    connection = get_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                manufacturer TEXT,
                model TEXT,
                serial_number TEXT UNIQUE,
                assigned_to TEXT,
                status TEXT NOT NULL DEFAULT 'available'
                    CHECK (status IN (
                        'available',
                        'in_use',
                        'repair',
                        'retired'
                    ))
            )
        """)

        connection.commit()

    finally:
        connection.close()
