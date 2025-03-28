import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()
passw = os.getenv("PASSWORD")

class CreateDatabase:
    def __init__(self):
        self.connection = self.create_connection()
        self.create_database()
        self.create_user_table()
        self.create_score_table()
    
    def create_connection(self):
        """Connect to mysql"""
        try:
            connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=passw
            )
            if connection.is_connected():
                print("Connecté à la base de donnée.")
            return connection
        except Error as error:
            print(f"Erreur : {error}")
            return None
    
    def create_database(self):
        """Create minesweeper database if it doesn't exist """
        cursor = self.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS minesweeper")
        print("Base de donnée crée: minesweeper")