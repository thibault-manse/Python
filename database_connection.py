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
    
    def close(self):
        """To close the database connection"""
        if self.db and self.db.is_connected():
            self.db.close()
            print("La connexion à la base de donnée est close.")
    
    def get_cursor(self):
        """To get cursor"""
        if self.db and self.db.is_connected():
            return self.db.cursor()
        else:
            raise Exception("La connexion à la base de donnée n'est pas établie.")
    
    def get_connection(self):
        """To return the database connection if it is active"""
        if self.db is not None and self.db.is_connected():
            return self.db
        else:
            raise Exception("La connexion à la base de donnée n'est pas établie.")