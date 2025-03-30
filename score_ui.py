import customtkinter as ctk

class ScoreUI:
    def __init__(self, root, score_manager):
        self.root = root
        self.score_manager = score_manager

    def open_hall_of_fame(self):
        hall_of_fame_window = ctk.CTkToplevel(self.root)
        hall_of_fame_window.title("Hall of Fame")
        hall_of_fame_window.geometry("300x400")

        scrollable_frame = ctk.CTkScrollableFrame(hall_of_fame_window)
        scrollable_frame.pack(fill="both", expand=True)

        scores = self.score_manager.get_scores()
        if scores:
            for username, score in scores.items():
                ctk.CTkLabel(scrollable_frame, text=f"{username}: {score}", font=("Arial", 12)).pack()

        back_button = ctk.CTkButton(hall_of_fame_window, text="Retour", command=hall_of_fame_window.destroy)
        back_button.pack(pady=10)