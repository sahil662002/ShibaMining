import sqlite3
import time

DB_NAME = "shibabot.db"


def connect():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Users Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        coins INTEGER DEFAULT 0,
        verified INTEGER DEFAULT 0,
        ref_by INTEGER DEFAULT 0,
        total_referrals INTEGER DEFAULT 0,
        join_date INTEGER DEFAULT 0
    )
    """)

    # Mining Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS mining (
        user_id INTEGER PRIMARY KEY,
        start_time INTEGER DEFAULT 0,
        end_time INTEGER DEFAULT 0,
        reward INTEGER DEFAULT 100,
        claimed INTEGER DEFAULT 1
    )
    """)

    # Settings Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY,
        mining_reward INTEGER DEFAULT 100,
        mining_time INTEGER DEFAULT 7200,
        referral_bonus INTEGER DEFAULT 200,
        first_withdraw INTEGER DEFAULT 5000,
        next_withdraw INTEGER DEFAULT 10000,
        withdraw_fee INTEGER DEFAULT 5
    )
    """)

    cur.execute(
        "INSERT OR IGNORE INTO settings(id) VALUES (1)"
    )

    conn.commit()
    conn.close()


def add_user(user_id, username, first_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT OR IGNORE INTO users
        (
            user_id,
            username,
            first_name,
            join_date
        )
        VALUES
        (
            ?, ?, ?, ?
        )
        """,
        (
            user_id,
            username,
            first_name,
            int(time.time())
        )
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
        return row["verified"] == 1

    return False

def get_balance(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT coins FROM users WHERE user_id = ?",
        (user_id,)
    )

    row = cur.fetchone()
    conn.close()

    if row:
        return row["coins"]

    return 0


def add_coins(user_id, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET coins = coins + ? WHERE user_id = ?",
        (amount, user_id)
    )

    conn.commit()
    conn.close()


def remove_coins(user_id, amount):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET coins = coins - ? WHERE user_id = ?",
        (amount, user_id)
    )

    conn.commit()
    conn.close()


def start_mining(user_id):
    conn = connect()
    cur = conn.cursor()

    start_time = int(time.time())
    end_time = start_time + 7200

    cur.execute(
        """
        INSERT OR REPLACE INTO mining
        (
            user_id,
            start_time,
            end_time,
            reward,
            claimed
        )
        VALUES
        (
            ?, ?, ?, ?, ?
        )
        """,
        (
            user_id,
            start_time,
            end_time,
            100,
            0
        )
    )

    conn.commit()
    conn.close()

def get_mining(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM mining WHERE user_id = ?",
        (user_id,)
    )

    row = cur.fetchone()
    conn.close()

    return row


def claim_mining(user_id):
    mining = get_mining(user_id)

    if not mining:
        return False

    current_time = int(time.time())

    if mining["claimed"] == 1:
        return False

    if current_time < mining["end_time"]:
        return False

    add_coins(user_id, mining["reward"])

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE mining SET claimed = 1 WHERE user_id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()

    return True


def get_settings():
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM settings WHERE id = 1"
    )

    row = cur.fetchone()

    conn.close()

    return row
