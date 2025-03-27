import customtkinter as ctk

class GameInfo:
    def __init__(self, root, mines, buttons):
        self.root = root
        self.mines = mines
        self.buttons = buttons
        self.flags = 0
        self.question_marks = 0
        
        self.create_info_labels()
        
    def create_info_labels(self):
        """ To display info label """
        self.mines_label = ctk.CTkLabel(self.root, text=f"Mines restantes : {self.mines}", font=("Arial", 14))
        self.mines_label.pack(pady=5)
        
        self.flags_label = ctk.CTkLabel(self.root, text=f"Drapeaux : {self.flags}", font=("Arial", 14))
        self.flags_label.pack(pady=5)
        
        self.question_marks_label = ctk.CTkLabel(self.root, text=f"Points d'interrogation : {self.question_marks}", font=("Arial", 14))
        self.question_marks_label.pack(pady=5)

    def update_mines(self, mines):
        """To update mines"""
        self.mines = mines
        self.mines_label.configure(text=f"Mines : {self.mines}")

    def update_flags(self, change):
        """To update flags"""
        self.flags += change
        self.flags_label.configure(text=f"Drapeaux : {self.flags}")