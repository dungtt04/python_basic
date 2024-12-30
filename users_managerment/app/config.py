import sqlite3

# filepath: /c:/Users/Admin/Desktop/aht/python-basic/users_managerment/app/config.py
DATABASE = 'path_to_your_database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    return conn