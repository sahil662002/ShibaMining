import sqlite3

DB_NAME = "shibabot.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        coins INTEGER DEFAULT 0,
        ref_by INTEGER DEFAULT 0,
        verified INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, username, first_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT OR IGNORE INTO users (user_id, username, first_name) VALUES (?, ?, ?)",
        (user_id, username, first_name)
    )

    conn.commit()
    conn.close()


def verify_user(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET verified = 1 WHERE user_id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()


def is_verified(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT verified FROM users WHERE user_id = ?",
        (user_id,)
    )

    row = cur.fetchone()

    conn.close()

    if row:
        return row[0] == 1

    return False
