import time


class Timer:
    def __init__(self):
        self.elapsed_time = 0
        self.is_running = False
        self.is_paused = True
        self.start_time = 0
    
    def start_timer(self):
        """ To start the timer"""
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.start_time = time.time()

    def pause_timer(self):
        """To pause the timer"""
        if self.is_running:
            self.is_running = False
            self.is_paused = True
            self.elapsed_time += time.time() - self.start_time
        elif self.is_paused:
            self.start_timer()
    
    def stop_timer(self):
        """To stop the timer"""
        if self.is_running:
            self.is_running = False
            self.elapsed_time += time.time() - self.start_time 
    
    def reset_timer(self):
        """To reset the timer"""
        self.elapsed_time = 0
        self.is_running = False
        self.is_paused = True
    
    def update_timer(self):
        """To update the timer"""
        total_seconds = int(self.elapsed_time + (time.time() - self.start_time) if self.is_running else self.elapsed_time)
        return divmod(total_seconds, 60)