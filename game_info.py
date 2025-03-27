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
        self.mines_label = ctk.CTkLabel(self.root, text=f"💣 : {self.mines}", font=("Arial", 14), text_color="orange")
        self.mines_label.pack(pady=5)
        
        self.flags_label = ctk.CTkLabel(self.root, text=f"🚩 : {self.flags}", font=("Arial", 14), text_color="orange")
        self.flags_label.pack(pady=5)
        
        self.question_marks_label = ctk.CTkLabel(self.root, text=f"? : {self.question_marks}", font=("Arial", 14), text_color="orange")
        self.question_marks_label.pack(pady=5)

    def update_mines(self, mines):
        """To update mines"""
        self.mines = mines
        self.mines_label.configure(text=f" 💣 : {self.mines}", font=("Arial", 14), text_color="orange")

    def update_flags(self, change):
        """To update flags"""
        self.flags += change
        self.flags_label.configure(text=f"🚩 : {self.flags}", font=("Arial", 14), text_color="orange")

    def update_question_marks(self, change):
        """To update question marks"""
        self.question_marks += change
        self.question_marks_label.configure(text=f"? : {self.question_marks}", font=("Arial", 14), text_color="orange")
    
    def update_info(self):
        """To update info"""
        self.update_mines(self.mines)
        self.update_flags(self.flags)
        self.update_question_marks(self.question_marks)
    
    def stop_updates(self):
        """To stop updates"""
        pass