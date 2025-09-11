import unittest
from pygame_rules.counters import Counter

class TestCounter(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_initial_value(self):
        self.assertEqual(self.counter.get_value(), 0)

    def test_increment(self):
        self.counter.increment()
        self.assertEqual(self.counter.get_value(), 1)

    def test_decrement(self):
        self.counter.increment()
        self.counter.decrement()
        self.assertEqual(self.counter.get_value(), 0)

    def test_reset(self):
        self.counter.increment()
        self.counter.reset()
        self.assertEqual(self.counter.get_value(), 0)

    def test_set_value(self):
        self.counter.set_value(10)
        self.assertEqual(self.counter.get_value(), 10)

    def test_on_change_event(self):
        changes = []
        def on_change(value):
            changes.append(value)

        self.counter.on_change = on_change
        self.counter.increment()
        self.assertEqual(changes, [1])

    def test_on_max_reached_event(self):
        changes = []
        def on_max_reached():
            changes.append("max reached")

        self.counter.on_max_reached = on_max_reached
        self.counter.set_value(5)
        self.counter.set_value(6)  # Assuming max is 5
        self.assertEqual(changes, ["max reached"])

    def test_on_min_reached_event(self):
        changes = []
        def on_min_reached():
            changes.append("min reached")

        self.counter.on_min_reached = on_min_reached
        self.counter.decrement()  # Assuming min is 0
        self.assertEqual(changes, ["min reached"])

if __name__ == '__main__':
    unittest.main()