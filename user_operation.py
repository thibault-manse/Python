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
            messagebox.showinfo("Info", f"'{username}', vous êtes enregistré.")
            return True
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Info",f"'{username}', vous êtes déja enregistré.")
            return False
        except Error as error:
            messagebox.showerror(f"Une erreur est survenue lors de l'enregistrement : {error}")