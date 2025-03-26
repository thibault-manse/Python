import time

class Timer:
    def __init__(self):
        self.elapsed_time = 0
        self.is_running = False
        self.is_paused = True
        self.start_time = 0
    
    def start(self):
        """ To start the timer """
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.start_time = time.time()

    def pause(self):
        """ Pause or restart the timer """
        if self.is_running:
            self.is_running = False
            self.is_paused = True
            self.elapsed_time += time.time() - self.start_time
        elif self.is_paused:
            self.start()
    
    def stop(self):
        """ Stop the timer """
        if self.is_running:
            self.is_running = False
            self.elapsed_time += time.time() - self.start_time 

    def reset(self):
        """ Reset the timer """
        self.elapsed_time = 0
        self.is_running = False
        self.is_paused = True

    