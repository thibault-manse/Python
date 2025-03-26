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
        self.stop_button.pack()

        self.reset_button = tk.Button(self.root, text="Réinitialiser", command=self.perform_reset_timer)
        self.reset_button.pack()

        self.update_timer_display()

    def perform_start_timer(self):
        """To perform the timer start"""
        self.timer.start_timer()
        self.update_timer_display()
    
    def perform_pause_timer(self):
        """To perform the timer pause method """
        self.timer.pause_timer()
    
    def perform_stop_timer(self):
        """To perform the timer stop method"""
        self.timer.stop_timer()

    def perform_reset_timer(self):
        """To perform the timer reset method"""
        self.timer.reset_timer()
        self.timer_label.config(text="Temps : 0.0")

    def update_timer_display(self):
        """To perform the update"""
        elapsed = self.timer.update_timer()
        self.timer_label.config(text=f"Temps : {elapsed:.1f}")
        self.root.after(100, self.update_timer_display) 

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerTest(root)
    root.mainloop()