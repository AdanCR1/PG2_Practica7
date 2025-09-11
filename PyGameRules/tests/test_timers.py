import unittest
from pygame_rules.timers import Timer

class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer()

    def test_start_timer(self):
        self.timer.start(5)
        self.assertTrue(self.timer.is_running)

    def test_stop_timer(self):
        self.timer.start(5)
        self.timer.stop()
        self.assertFalse(self.timer.is_running)

    def test_pause_timer(self):
        self.timer.start(5)
        self.timer.pause()
        self.assertTrue(self.timer.is_paused)

    def test_resume_timer(self):
        self.timer.start(5)
        self.timer.pause()
        self.timer.resume()
        self.assertFalse(self.timer.is_paused)

    def test_timer_completion_callback(self):
        completed = False

        def callback():
            nonlocal completed
            completed = True

        self.timer.start(1, callback)
        self.timer.update(1)  # Simulate time passing
        self.assertTrue(completed)

    def test_cooldown_reusability(self):
        self.timer.start(2)
        self.timer.stop()
        self.timer.start(2)
        self.assertTrue(self.timer.is_running)

if __name__ == '__main__':
    unittest.main()