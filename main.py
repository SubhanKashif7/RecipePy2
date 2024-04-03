from DatabaseOperations import DatabaseOperations
from Api_Request import Api_Request
from Methods import Methods
import sqlite3
conn = sqlite3.connect("recipe.db")
operations = DatabaseOperations(conn)
methods = Methods()

while True:
    print("1. Register User")
    print("2. Login User")
    print("3. Exit")
    choice = int(input("Enter Your Choice:  "))
