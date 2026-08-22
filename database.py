import os

import mysql.connector
from dotenv import load_dotenv


class Database:
    def __init__(self):
        load_dotenv()

        self.conn = mysql.connector.connect(
            host= os.getenv("MYSQL_HOST"),
            user= os.getenv("MYSQL_USER"),
            password= os.getenv("MYSQL_PASSWORD"),
            database= os.getenv("MYSQL_DATABASE")
)
        self.cursor = self.conn.cursor()

        # create users table
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    chat_id BIGINT UNIQUE
)        
    """);

        self.conn.commit()

    # save users in db
    def add (self,chat_id):

        self.cursor.execute(
    "INSERT IGNORE INTO users(chat_id) VALUES(%s)",
    (chat_id,)
)

        self.conn.commit()


    def get_users(self):

        

        self.cursor.execute(
            "SELECT chat_id FROM users"
        )

        users = self.cursor.fetchall()
        return users
    def close(self):
        self.cursor.close()
        self.conn.close()