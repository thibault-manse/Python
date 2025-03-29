import os
from mysql.connector import Error
import mysql.connector
from customtkinter import messagebox
import hashlib
import secrets
from dotenv import load_dotenv
from database_connection import Database

load_dotenv()
passw = os.getenv("PASSWORD")
pepper = os.getenv("PEPPER")

class UserOperations:
    def __init__(self, db: Database):
        self.db = db
        self.user_id = None
        self.cursor = self.db.get_cursor()
        self.connection = self.db.get_connection()

    def hash_password(self, password, salt):
        """To hash the password"""
        return hashlib.sha256((password + salt + pepper).encode()).hexdigest()
    
    def generate_salt(self):
        """To generate random salt"""
        return secrets.token_hex(16)

    def validate_username(self, username):
        """To validate username"""
        if not username or len(username) <= 4 or not username.isalpha():
            return False
        return True
    
    def is_usernam_taken(self, username):
        """To check if the username already exist in the database"""
        self.cursor.execute("SELECT COUNT (*) FROM users WHERE username = %s ", (username,))
        return self.cursor.fetchone()[0]>0

    def register_user(self, username, password):
        """ To register a new user """
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            messagebox.showinfo("Info", f"Bienvenue {username}.")
            return True
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Info",f"{username} est déja utilisé!\nConnectez vous,o\nou choississez un autre username.")
            return False # method had to change here
        except Error as error:
            messagebox.showerror(f"Une erreur est survenue lors de l'enregistrement : {error}")


        
                