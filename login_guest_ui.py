import customtkinter as ctk
from registration_ui import RegistrationUi 
from user_operation import UserOperations
from database_connection import Database

class LoginGuestUi:
    def __init__(self, master):
        self.master = master
        self.master.title("Démineur")

        self.welcome_label = ctk.CTkLabel(master, text="Bienvenue", font=("Arial", 18, "bold"))
        self.welcome_label.pack(pady=10)

        self.connect_label = ctk.CTkLabel(master, text="Se Connecter", font=("Arial" , 14))
        self.connect_label.pack(pady=5)

        self.username_label = ctk.CTkLabel(master, text="Nom d'utilisateur :")
        self.username_label.pack()
        self.username_entry = ctk.CTkEntry(master)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(master, text="Mot de Passe :")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(master, show="*")
        self.password_entry.pack()

        self.play_button = ctk.CTkButton(master, text="JOUER", command=self.login)
        self.play_button.pack(pady=5)
        
        self.new_user_label = ctk.CTkLabel(master, text="Nouveau joueur ?\nCréer un Compte")
        self.new_user_label.pack(pady=5)

        self.register_button = ctk.CTkButton(master, text="S'ENREGISTER", command=self.show_register_form)
        self.register_button.pack(pady=5)

        self.guest_button = ctk.CTkButton(master, text="Jouer comme invité", command=self.play_as_guest)
        self.guest_button.pack(pady=5)

    def login(self):
        """To perform the login"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        db = Database()
        user_operation = UserOperations(db)
        user_operation.login_user(username, password)

    def show_register_form(self):
        """To open the register form window"""
        RegistrationUi(self.master)

    def play_as_guest(self):
        """To perform play as guest"""
        # add logic to start the game as guest
        pass

