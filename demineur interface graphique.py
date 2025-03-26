import customtkinter as ctk
import random

class Minesweeper:
    COLORS = {
        1: "#0000FF",  # Bleu
        2: "#008000",  # Vert
        3: "#FF0000",  # Rouge
        4: "#800080",  # Violet
        5: "#8B4513",  # Marron
        6: "#00CED1",  # Turquoise
        7: "#000000",  # Noir
        8: "#696969"   # Gris foncé
    }

    def __init__(self, root, rows=10, cols=10, mines=15):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = []
        self.mine_positions = set()
        self.revealed = set()
        self.marked = {}  

        # Cadre principal
        self.main_frame = ctk.CTkFrame(root, fg_color="#404040")
        self.main_frame.pack(fill="both", expand=True)

        # Espace à gauche pour les futurs boutons/infos
        self.side_frame = ctk.CTkFrame(self.main_frame, width=200, fg_color="#303030")
        self.side_frame.pack(side="left", fill="y")

        # Cadre de la grille
        self.grid_frame = ctk.CTkFrame(self.main_frame, fg_color="#505050")
        self.grid_frame.pack(side="right", padx=20, pady=20)

        self.create_widgets()
        self.place_mines()

    def create_widgets(self):
        for row in range(self.rows):
            row_buttons = []
            for col in range(self.cols):
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

    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            self.mine_positions.add((row, col))

    def on_click(self, row, col):
        
        if self.marked[(row, col)] is not None or (row, col) in self.revealed:
            return

        if (row, col) in self.mine_positions:
            self.buttons[row][col].configure(text='💣', fg_color='red')
            self.game_over()
        else:
            self.reveal(row, col)

    def on_right_click(self, row, col):
        
        if (row, col) in self.revealed:
            return

        if self.marked[(row, col)] is None:
            self.marked[(row, col)] = "?"
            self.buttons[row][col].configure(text="?", text_color="red")
        elif self.marked[(row, col)] == "?":
            self.marked[(row, col)] = "🚩"
            self.buttons[row][col].configure(text="🚩", text_color="red")
        else:
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
        count = 0
        for r in range(max(0, row-1), min(self.rows, row+2)):
            for c in range(max(0, col-1), min(self.cols, col+2)):
                if (r, c) in self.mine_positions:
                    count += 1
        return count


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Démineur")
    game = Minesweeper(root)
    root.mainloop()
