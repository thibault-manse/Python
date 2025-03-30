import customtkinter as ctk 
from user_operation import UserOperations
from database_connection import Database
from login_guest_ui import LoginGuestUi

class RegistrationUi:
    def __init__(self, master):
        self.master = master
        self.master.title("Inscription")

        self.register_label = ctk.CTkLabel(master, text="Créer un compte", font=("Arial", 18, "bold"))
        self.register_label.pack(pady=10)

        self.username_label = ctk.CTkLabel(master, text="Nom d'utilisateur :")
        self.username_label.pack()
        self.username_entry = ctk.CTkEntry(master)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(master, text="Mot de passe :")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(master, show="*")
        self.password_entry.pack()

        self.confirm_password_label = ctk.CTkLabel(master, text="Confirmez le mot de passe :")
        self.confirm_password_label.pack()
        self.confirm_password_entry = ctk.CTkEntry(master, show="*")
        self.confirm_password_entry.pack()

        self.show_password_var = ctk.BooleanVar()
        self.show_password_checkbox = ctk.CTkCheckBox(master, text="Afficher le mot de passe", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.show_password_checkbox.pack()

        self.register_button = ctk.CTkButton(master, text="S'ENREGISTRER", command=self.register)
        self.register_button.pack(pady=5)

    def toggle_password_visibility(self):
        """To toggle the password visibility"""
        if self.show_password_var.get():
            self.password_entry.configure(show="")
            self.confirm_password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
            self.confirm_password_entry.configure(show="*")

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
