import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
passw = os.getenv("PASSWORD")

class Database:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password=passw,
                database="minesweeper"
            )
            print("La connexion à la base de donnée est active.")
        except mysql.connector.Error as databaseerror:
            print(f"Une erreur est survenue lors de la connextion : {databaseerror}")
            self.db=None
    