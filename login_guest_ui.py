import customtkinter as ctk
from user_operation import UserOperations
from database_connection import Database
from MinesweeperApp import Minesweeper

class LoginGuestUi:
    def __init__(self, master):
        self.master = master
        self.master.title("Démineur")
        self.master.geometry("300x430")
        self.create_login_ui() 

    def create_login_ui(self):
        self.clear_ui()    
        self.welcome_label = ctk.CTkLabel(self.master, text="BIENVENUE", font=("Arial", 18, "bold"))
        self.welcome_label.pack(pady=10)

        self.connect_label = ctk.CTkLabel(self.master, text="SE CONNECTER", font=("Arial" , 14))
        self.connect_label.pack(pady=5)

        self.username_label = ctk.CTkLabel(self.master, text="Nom d'utilisateur :")
        self.username_label.pack()
        self.username_entry = ctk.CTkEntry(self.master)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(self.master, text="Mot de Passe :")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self.master, show="*")
        self.password_entry.pack()

        self.show_password_var = ctk.BooleanVar()
        self.show_password_checkbox = ctk.CTkCheckBox(self.master, text="Afficher le mot de passe", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.show_password_checkbox.pack(pady=10)

        self.play_button = ctk.CTkButton(self.master, text="JOUER", command=self.login)
        self.play_button.pack(pady=10)
        
        self.new_user_label = ctk.CTkLabel(self.master, text="Nouveau joueur ?")
        self.new_user_label.pack(pady=5)

        self.register_button = ctk.CTkButton(self.master, text="Créer un Compte", command=self.create_register_ui)
        self.register_button.pack(pady=5)

        self.guest_button = ctk.CTkButton(self.master, text="Jouer comme invité", command=self.play_as_guest)
        self.guest_button.pack(pady=5)
    
    def create_register_ui(self):
        self.clear_ui()

        self.register_label = ctk.CTkLabel(self.master, text="Créer un compte", font=("Arial", 18, "bold"))
        self.register_label.pack(pady=10)

        self.username_label = ctk.CTkLabel(self.master, text="Nom d'utilisateur :")
        self.username_label.pack()
        self.username_entry = ctk.CTkEntry(self.master)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(self.master, text="Mot de passe :")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self.master, show="*")
        self.password_entry.pack()

        self.confirm_password_label = ctk.CTkLabel(self.master, text="Confirmez le mot de passe :")
        self.confirm_password_label.pack()
        self.confirm_password_entry = ctk.CTkEntry(self.master, show="*")
        self.confirm_password_entry.pack()

        self.show_password_var = ctk.BooleanVar()
        self.show_password_checkbox = ctk.CTkCheckBox(self.master, text="Afficher le mot de passe", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.show_password_checkbox.pack(pady=10)

        self.register_button = ctk.CTkButton(self.master, text="S'ENREGISTRER", command=self.register)
        self.register_button.pack(pady=10)   

        self.back_to_login_button = ctk.CTkButton(self.master, text="Retour", command=self.create_login_ui, fg_color="transparent", hover_color=self.master.cget("bg"), text_color="white")
        self.back_to_login_button.pack(pady=5)     

    def toggle_password_visibility(self):
        """To toggle the password visibility"""
        if self.show_password_var.get():
            self.password_entry.configure(show="")
            self.confirm_password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
            self.confirm_password_entry.configure(show="*")

    def login(self):
        """To perform the login"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        db = Database()
        user_operation = UserOperations(db)
        user_id = user_operation.login_user(username, password)
        if user_id is not None:
            self.master.destroy()
            new_root = ctk.CTk()
            Minesweeper(new_root, user_id, db=db)
            new_root.mainloop()

    def register(self):
        """To perform registering process"""
        username = self.username_entry.get()
        password1 = self.password_entry.get()
        password2 = self.confirm_password_entry.get()
        db=Database()
        user_operation = UserOperations(db)
        registration_successful = user_operation.register_user(username, password1, password2)
        if registration_successful:
            self.master.destroy()
            new_root = ctk.CTk()
            LoginGuestUi(new_root)
            new_root.mainloop()

    def clear_ui(self):
        """Clear the window"""
        for widget in self.master.winfo_children():
            widget.destroy()

    def play_as_guest(self):
        """To perform play as guest"""
        db = Database()
        self.master.destroy()
        new_root = ctk.CTk()
        Minesweeper(new_root, db=db)
        new_root.mainloop()

