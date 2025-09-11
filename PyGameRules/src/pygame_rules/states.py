class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, on_enter=None, on_exit=None, on_update=None):
        self.states[name] = {
            'on_enter': on_enter,
            'on_exit': on_exit,
            'on_update': on_update
        }

    def change_state(self, name):
        if self.current_state is not None:
            self.exit_current_state()
        self.current_state = name
        self.enter_current_state()

    def enter_current_state(self):
        if self.current_state in self.states and self.states[self.current_state]['on_enter']:
            self.states[self.current_state]['on_enter']()

    def exit_current_state(self):
        if self.current_state in self.states and self.states[self.current_state]['on_exit']:
            self.states[self.current_state]['on_exit']()

    def update(self):
        if self.current_state in self.states and self.states[self.current_state]['on_update']:
            self.states[self.current_state]['on_update']()