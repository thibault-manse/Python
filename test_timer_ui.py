import tkinter as tk 
from timer import Timer

class TimerTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Chrono Test")

        self.timer = Timer()

        self.timer_label = tk.Label(self.root, text="Temps : 0.0")
        self.timer_label.pack()

        self.start_button = tk.Button(self.root, text="Démarrer", command=self.perform_start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.perform_pause_timer)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.perform_stop_timer) 
        self.pause_button.pack()

        self.reset_button = tk.Button(self.root, text="Réinitialiser", command=self.perform_reset_timer)
        self.reset_button.pack()

        self.update_timer_display()

    def perform_start_timer(self):
        self.timer.start_timer()
        self.update_timer_display()
