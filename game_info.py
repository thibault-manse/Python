import customtkinter as ctk

class GameInfo:
    def __init__(self, root, mines, buttons):
        self.root = root
        self.mines = mines
        self.buttons = buttons
        self.flags = 0
        self.question_marks = 0
        
        self.create_info_labels()
        
