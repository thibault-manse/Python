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
    
    def validate_password(self,password):
        """To validate password before hashing and registering in database"""
        if (len(password) < 10 or
            not any(character.isupper() for character in password)
            or not any(character.islower() for character in password)
            or not any(character.isdigit() for character in password)
            or not any(character in '?./§¨£µ%°,;:!^$*+-_|[{#~&@]^}=()]' for character in password)):
            return False
        return True

    def register_user(self, username, password1, password2):
        """ To register a new user """
        if not self.validate_username(username):
            messagebox.showerror("Erreur", "Le nom d'utilisateur doit contenir\nuniquement des lettres et être\nplus long que 4 caractères. ")
            return False
        if self.is_usernam_taken(username):
            messagebox.showinfo("Info", f"{username} est déja utilisé !\nVeuillez choisir un autre nom d'utlisateur\nou vous connecter. ")
            return False
        if password1 != password2:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
            return False
        if not self.validate_password(password1):
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins\n10 caractères, y compris des majuscules,\ndes minuscules et des caractères spéciaux.")
            return False

        salt = self.generate_salt()
        hashed_password = self.hash_password(password1, salt) 

        try:
            self.cursor.execute("INSERT INTO users (username, password, salt) VALUES (%s, %s)", (username, hashed_password, salt))
            self.connection.commit()
            messagebox.showinfo("Info", f"Bienvenue {username}.")
            return True
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Info",f"{username} est déja utilisé!\nConnectez vous,\nou choississez un autre nom d'utilisateur.")
            return False
        except Error as error:
            messagebox.showerror(f"Une erreur est survenue lors de l'enregistrement : {error}")
            return False

    def login_user(self, username, password):
        pass
        
                