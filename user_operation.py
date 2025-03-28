import os
from mysql.connector import Error
import mysql.connector
from customtkinter import messagebox
import hashlib
import secrets
from dotenv import load_dotenv
from database_connection import Database
import re

load_dotenv()
passw = os.getenv("PASSWORD")
pepper = os.getenv("PEPPER")

class UserOperations:
    def __init__(self, db: Database):
        self.db = db
        self.user_id = None

    

    def register_user(self, username, password):
        """ To register a new user """
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            messagebox.showinfo("Info", f"Bienvenue {username}.")
            return True
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Info",f"{username}, vous avez déja un compte.")
            return False
        except Error as error:
            messagebox.showerror(f"Une erreur est survenue lors de l'enregistrement : {error}")


        
                