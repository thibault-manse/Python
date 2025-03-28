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
        
    def get_scores(self):
        """To display scores ordered by descending values"""
        try:
            self.cursor.execute("""
                SELECT users.username, scores.score FROM scores
                JOIN users ON scores.user_id = users.id
                ORDER BY scores.score DESC""")
            results = self.cursor.fetchall()
            hall_of_fame = {username: score for username, score in results}
            return hall_of_fame
        except Error as error:
            messagebox.showerror("Erreur", f"Erreur lors de la récupération des scores : {error}")
            return None
        
                