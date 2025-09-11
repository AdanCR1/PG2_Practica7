# File: /PyGameRules/PyGameRules/src/pygame_rules/types.py

# This file contains type definitions and constants used throughout the library.

from enum import Enum

class GameState(Enum):
    PLAY = "play"
    PAUSE = "pause"
    MENU = "menu"
    GAME_OVER = "game_over"

# Constants
DEFAULT_LIFE_COUNT = 3
DEFAULT_SCORE = 0
TIMER_TICK_INTERVAL = 100  # milliseconds

# Type aliases
CounterType = int
TimerType = float
StateType = GameState