class Timer:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False
        self.paused = False
        self.callback = None

    def start(self):
        if not self.running:
            self.start_time = pygame.time.get_ticks() - self.elapsed_time
            self.running = True
            self.paused = False

    def stop(self):
        self.running = False
        self.elapsed_time = 0

    def pause(self):
        if self.running and not self.paused:
            self.elapsed_time = pygame.time.get_ticks() - self.start_time
            self.paused = True

    def resume(self):
        if self.paused:
            self.start_time = pygame.time.get_ticks() - self.elapsed_time
            self.running = True
            self.paused = False

    def update(self):
        if self.running:
            current_time = pygame.time.get_ticks()
            if self.callback and current_time - self.start_time >= self.elapsed_time:
                self.callback()
                self.stop()

    def set_callback(self, callback):
        self.callback = callback

    def get_elapsed_time(self):
        if self.running:
            return pygame.time.get_ticks() - self.start_time
        return self.elapsed_time

    def is_running(self):
        return self.running

    def is_paused(self):
        return self.paused