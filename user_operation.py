import os

from mysql.connector import Error
import mysql.connector
from customtkinter import messagebox

class UserOperations:
    def __init__(self,cursor, connection):
        self.cursor = cursor
        self.connection = connection

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

    def update_score(self, user_id, score):
        """To update the score for a registred user """
        try:
            self.cursor.execute("INSERT INTO scores (user_id, score) VALUES (%s, %s)", (user_id, score))
            self.connection.commit()
            messagebox.showinfo("Info","Votre score a été mis à jour.")
        except Error as error:
            messagebox.showerror("Erreur", f"Votre score n'a pas pu être mis à jour : {error}")