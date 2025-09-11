import unittest
from pygame_rules.states import StateMachine, State

class TestStateMachine(unittest.TestCase):

    def setUp(self):
        self.state_machine = StateMachine()
        self.state_machine.add_state(State("MENU"))
        self.state_machine.add_state(State("PLAY"))
        self.state_machine.add_state(State("PAUSE"))
        self.state_machine.add_state(State("GAME_OVER"))

    def test_initial_state(self):
        self.assertEqual(self.state_machine.current_state, "MENU")

    def test_transition_to_play(self):
        self.state_machine.change_state("PLAY")
        self.assertEqual(self.state_machine.current_state, "PLAY")

    def test_transition_to_pause(self):
        self.state_machine.change_state("PLAY")
        self.state_machine.change_state("PAUSE")
        self.assertEqual(self.state_machine.current_state, "PAUSE")

    def test_transition_to_game_over(self):
        self.state_machine.change_state("GAME_OVER")
        self.assertEqual(self.state_machine.current_state, "GAME_OVER")

    def test_invalid_transition(self):
        with self.assertRaises(ValueError):
            self.state_machine.change_state("INVALID_STATE")

    def test_on_enter_callback(self):
        entered_state = []

        def on_enter_play():
            entered_state.append("PLAY")

        self.state_machine.add_state(State("PLAY", on_enter=on_enter_play))
        self.state_machine.change_state("PLAY")
        self.assertIn("PLAY", entered_state)

    def test_on_exit_callback(self):
        exited_state = []

        def on_exit_play():
            exited_state.append("PLAY")

        self.state_machine.add_state(State("PLAY", on_exit=on_exit_play))
        self.state_machine.change_state("PLAY")
        self.state_machine.change_state("MENU")
        self.assertIn("PLAY", exited_state)

if __name__ == '__main__':
    unittest.main()