import sqlite3
from app.config import DATABASE

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    with open('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

class UserModel:
    def __init__(self):
        self.db = get_db()

    def fetch_all_users(self):
        cursor = self.db.execute('SELECT * FROM users')
        return cursor.fetchall()

    def create_user(self, name, email, password):
        self.db.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        self.db.commit()

    def update_user(self, user_id, name, email, password):
        self.db.execute('UPDATE users SET name = ?, email = ?, password = ? WHERE id = ?', (name, email, password, user_id))
        self.db.commit()

    def delete_user(self, user_id):
        self.db.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.db.commit()