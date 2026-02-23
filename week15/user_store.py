import sqlite3

class UserStore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def load(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT id, name, email FROM users')
        rows = c.fetchall()
        conn.close()
        return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]

    def find_by_id(self, user_id):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT id, name, email FROM users WHERE id=?', (user_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}
        return None

    def save(self, user):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        if "id" in user and self.find_by_id(user["id"]):
            # update existing user
            c.execute('UPDATE users SET name=?, email=? WHERE id=?',
                      (user["name"], user["email"], user["id"]))
        else:
            # insert new user
            c.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                      (user["name"], user["email"]))
            user["id"] = c.lastrowid
        conn.commit()
        conn.close()
        return user

    def update_user(self, user_id, updated_data):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('UPDATE users SET name=?, email=? WHERE id=?',
                  (updated_data["name"], updated_data["email"], user_id))
        success = c.rowcount > 0
        conn.commit()
        conn.close()
        return success

    def delete_user(self, user_id):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE id=?', (user_id,))
        success = c.rowcount > 0
        conn.commit()
        conn.close()
        return success

    def get_next_id(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT MAX(id) FROM users')
        row = c.fetchone()
        conn.close()
        if row and row[0]:
            return row[0] + 1
        return 1