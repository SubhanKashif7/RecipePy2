import time
from Methods import Methods  # Assuming Methods is a custom module you've created

class DatabaseOperations:
    def __init__(self, connection):
        self._connection = connection
        self.c = self._connection.cursor()
        self.mymethods = Methods()

        # Create users table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE,
                            password TEXT
                        )''')
        self._connection.commit()

        # Create recipe table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS recipe (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            instruction TEXT NOT NULL,
                            status INTEGER NOT NULL,
                            time TEXT NOT NULL,
                            user_id INTEGER,
                            FOREIGN KEY (user_id) REFERENCES users(id)
                        )''')
        self._connection.commit()

    def get_recipe(self, recipe_id):
        self.c.execute("SELECT * FROM recipe WHERE id=?", (recipe_id,))
        recipe = self.c.fetchone()
        return recipe

    def register_user(self, username, password):
        self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self._connection.commit()

    def login_user(self, username, password):
        self.c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.c.fetchone()
        if user and user[2] == password:
            return user
        else:
            return None

    def add_recipe(self, title, instructions, ingredients, status, user_id):
        self.c.execute("INSERT INTO recipe (title, instruction, ingredients, status, time, user_id) VALUES (?, ?, ?, ?, ?, ?)",
                        (title, instructions, ingredients, status, time.ctime(), user_id))
        self._connection.commit()

    def get_all_recipe(self):
        self.c.execute("SELECT * FROM recipe")
        recipes = self.c.fetchall()
        for recipe in recipes:
            self.mymethods.spacer()
            print(recipe)
            self.mymethods.spacer()

    def update_recipe(self, recipe_id, title, instructions, ingredients, status):
        self.c.execute("UPDATE recipe SET title=?, instruction=?, ingredients=?, status=? WHERE id=?",
                        (title, instructions, ingredients, status, recipe_id))
        self._connection.commit()

    def delete_recipe(self, recipe_id):
        self.c.execute("DELETE FROM recipe WHERE id=?", (recipe_id,))
        self._connection.commit()

    def clear_database(self):
        self.c.execute("DELETE FROM users")
        self.c.execute("DELETE FROM recipe")
        self._connection.commit()
