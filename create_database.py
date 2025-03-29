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
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS minesweeper")
            print("Base de donnée crée: minesweeper")
        except Error as error:
            print(f"Erreur lors de la création de la base de donnée : {error}")
    
    def create_user_table(self):
        """Create the users table"""
        cursor = self.connection.user()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY, 
                        username VARCHAR(100) UNIQUE NOT NULL, 
                        password VARCHAR(100) NOT NULL,
                        salt VARCHAR(255)NOT NULL)
                           """)
            self.connection.commit()
            print("La table Users a été crée ou existe déja.")
        except Error as error:
            print(f"Erreur lors de la création de la table users : {error}")

    def create_score_table(self):
        """Create the scores table"""
        cursor = self.connection.score()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS scores (
                           score_id INT AUTO_INCREMENT PRIMARY KEY,
                           user_id INT NOT NULL,
                           score INT,
                           FOREIGN KEY (user_id) REFERENCES users(id))
                           """)
            self.connection.commit()
            print("La table scores a été crée ou existe déja.")
        except Error as error:
            print(f"Erreur lors de la création de la table scores : {error}")

    