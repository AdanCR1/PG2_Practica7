class Counter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Counter, cls).__new__(cls)
            cls._instance.value = 0
            cls._instance.max_value = None
            cls._instance.min_value = 0
            cls._instance.on_change = []
            cls._instance.on_max_reached = []
            cls._instance.on_min_reached = []
        return cls._instance

    def increment(self, amount=1):
        self.value += amount
        self._trigger_on_change()
        if self.max_value is not None and self.value >= self.max_value:
            self._trigger_on_max_reached()

    def decrement(self, amount=1):
        self.value -= amount
        self._trigger_on_change()
        if self.value <= self.min_value:
            self._trigger_on_min_reached()

    def reset(self):
        self.value = 0
        self._trigger_on_change()

    def set_value(self, value):
        self.value = value
        self._trigger_on_change()
        if self.max_value is not None and self.value >= self.max_value:
            self._trigger_on_max_reached()
        if self.value <= self.min_value:
            self._trigger_on_min_reached()

    def _trigger_on_change(self):
        for callback in self.on_change:
            callback(self.value)

    def _trigger_on_max_reached(self):
        for callback in self.on_max_reached:
            callback(self.value)

    def _trigger_on_min_reached(self):
        for callback in self.on_min_reached:
            callback(self.value)

    def set_max_value(self, max_value):
        self.max_value = max_value

    def set_min_value(self, min_value):
        self.min_value = min_value