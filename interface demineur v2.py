import customtkinter as ctk
import random
from TimerCount import Timer
from game_info import GameInfo


class Minesweeper:
    COLORS = {
        1: "#0000FF",
        2: "#008000",
        3: "#FF0000",
        4: "#800080",
        5: "#8B4513",
        6: "#00CED1",
        7: "#000000",
        8: "#696969"
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        
        self.timer = Timer()

        self.mines =0 # add this line

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(pady=20, padx=20)

        # Cadre gauche 
        self.left_frame = ctk.CTkFrame(self.main_frame, width=200, height=400)
        self.left_frame.pack(side="left", fill="y", padx=10)

        self.title_label = ctk.CTkLabel(self.left_frame, text="MINESWEEPER", font=("Arial", 18, "bold"), text_color="red")
        self.title_label.pack(pady=10)

        self.game_info = GameInfo(self.left_frame, 0, []) # add this line
        
        self.status_label = ctk.CTkLabel(self.left_frame, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)
        
        self.timer_label = ctk.CTkLabel(self.left_frame, text="Temps : 0s", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        self.pause_button = ctk.CTkButton(self.left_frame, text="Pause", command=self.toggle_pause)
        self.pause_button.pack(pady=5)

        ctk.CTkLabel(self.left_frame, text="Sélectionner une difficulté :", font=("Arial", 14)).pack()

        ctk.CTkButton(self.left_frame, text="Facile", command=lambda: self.start_game(5, 5, 5)).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Moyen", command=lambda: self.start_game(10, 10, 20)).pack(pady=5)
        ctk.CTkButton(self.left_frame, text="Difficile", command=lambda: self.start_game(15, 15, 50)).pack(pady=5)

        self.grid_frame = ctk.CTkFrame(self.main_frame)
        self.grid_frame.pack(side="right", padx=20)
        
        self.update_timer_display()
        
    def update_timer_display(self):
        minutes, seconds = self.timer.update_timer()
        self.timer_label.configure(text=f" chronomètre: {minutes}m: {seconds}s")
        self.root.after(1000, self.update_timer_display)
        
    

    def start_game(self, rows, cols, mines):
        
        self.mines = mines # add this line

        self.timer.reset_timer()
        self.timer.start_timer()

        self.game_info.update_flags(-self.game_info.flags)  # add this line  
        self.game_info.update_question_marks(-self.game_info.question_marks) # add this line
        self.game_info.update_mines(self.mines) # add this line
        
        self.status_label.configure(text="")
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.first_click = True
        self.mine_positions = set()
        self.revealed = set()
        self.marked = {}
        self.game_over_flag = False  

        self.buttons = []
        for row in range(rows):
            row_buttons = []
            for col in range(cols):
                btn = ctk.CTkButton(
                    self.grid_frame,
                    text='',
                    width=40,
                    height=40,
                    fg_color='#C0C0C0',
                    hover_color='#A9A9A9',
                    border_color='#808080',
                    border_width=2,
                    corner_radius=0,
                    font=ctk.CTkFont(family="Courier", size=16),
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.bind("<Button-3>", lambda event, r=row, c=col: self.on_right_click(r, c))
                row_buttons.append(btn)
                self.marked[(row, col)] = None
            self.buttons.append(row_buttons)

    def place_mines(self, exclude_row, exclude_col):
        
        while len(self.mine_positions) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) != (exclude_row, exclude_col) and (row, col) not in self.mine_positions:
                self.mine_positions.add((row, col))
    
    def toggle_pause(self):
        self.timer.pause_timer()

    def on_click(self, row, col):
        
        if self.game_over_flag or self.marked[(row, col)] is not None or (row, col) in self.revealed:
            return

        if self.first_click:
            self.place_mines(row, col)
            self.first_click = False

        if (row, col) in self.mine_positions:
            self.endgame(False)  
        else:
            self.reveal(row, col)
            if self.empty_board():
                self.endgame(True)  # Victoire

    def on_right_click(self, row, col):
        
        if self.game_over_flag or (row, col) in self.revealed:
            return

        if self.marked[(row, col)] is None:
            self.marked[(row, col)] = "🚩"
            self.buttons[row][col].configure(text="🚩", text_color="red")
            self.game_info.update_flags(+1) # add this line
        elif self.marked[(row, col)] == "🚩":
            self.marked[(row, col)] = "?"
            self.buttons[row][col].configure(text="?", text_color="orange")
            self.game_info.update_flags(-1) # add this line
            self.game_info.update_question_marks(+1) #add this line
        else:
            if self.marked[(row, col)] == "?": # add this line
                self.game_info.update_question_marks(-1) # add this line
            self.marked[(row, col)] = None
            self.buttons[row][col].configure(text="")

    def reveal(self, row, col):
        
        if (row, col) in self.revealed:
            return

        self.revealed.add((row, col))
        count = self.count_adjacent_mines(row, col)
        color = self.COLORS.get(count, "black")

        self.buttons[row][col].configure(
            text=str(count) if count > 0 else '',
            fg_color='white',
            text_color=color
        )

        if count == 0:
            for r in range(max(0, row-1), min(self.rows, row+2)):
                for c in range(max(0, col-1), min(self.cols, col+2)):
                    if (r, c) != (row, col):
                        self.reveal(r, c)

    def count_adjacent_mines(self, row, col):
        """ Compte le nombre de mines autour """
        count = 0
        for r in range(max(0, row-1), min(self.rows, row+2)):
            for c in range(max(0, col-1), min(self.cols, col+2)):
                if (r, c) in self.mine_positions:
                    count += 1
        return count

    def empty_board(self):
        
        return len(self.revealed) == (self.rows * self.cols - self.mines)
    
    

    def endgame(self, victory):
        
        self.timer.stop_timer()
        self.game_info.stop_updates() # add this line
        self.game_over_flag = True

        if victory:
            self.status_label.configure(text="🎉 Victoire ! 🎉", text_color="green")
            for row, col in self.mine_positions:
                self.buttons[row][col].configure(text="🚩", text_color="green")
        else:
            self.status_label.configure(text="💥 BOOM ! Vous avez perdu ! 💥", text_color="red")
            for row, col in self.mine_positions:
                self.buttons[row][col].configure(text='💣', fg_color='red')

        # Désactiver tous les boutons
        for row in self.buttons:
            for btn in row:
                btn.configure(state="disabled")

if __name__ == "__main__":
    root = ctk.CTk()
    game = Minesweeper(root)
    root.mainloop()
