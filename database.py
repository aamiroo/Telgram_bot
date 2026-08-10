import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("chatid.db")
        self.cursor = self.conn.cursor()

        # create users table
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id INTEGER UNIQUE)               
    """);

        self.conn.commit()
        self.conn.close()

    # save users in db
    def add (self,chat_id):
        self.conn = sqlite3.connect("chatid.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            "INSERT OR IGNORE INTO users(chat_id) VALUES(?)",
            (chat_id,)
        )

        self.conn.commit()
        self.conn.close()


    def get_users(self):

        self.conn = sqlite3.connect("chatid.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            "SELECT chat_id FROM users"
        )

        users = self.cursor.fetchall()
        return users
    def close(self):
        self.conn.close()