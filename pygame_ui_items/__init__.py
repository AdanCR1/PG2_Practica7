"""
pygame_ui_items - Librería para creación de elementos UI en Pygame
Versión 0.1.0
"""

from pygame_ui_items.ui_element import UIElement
from pygame_ui_items.button import *
from pygame_ui_items.button_factory import *
from pygame_ui_items.ui_manager import UIManager
from pygame_ui_items.event_queue import EventQueue, UIEvent
from pygame_ui_items.window_stack import Window, WindowStack
from pygame_ui_items.modal import *

__version__ = "0.1.0"
__all__ = [
    # Base
    "UIElement",
    "UIManager",
    
    # Buttons
    "Button",
    "RedButton",
    "BlueButton",
    "GreenButton",
    "YellowButton",
    "create_button",
    "button_red",
    "button_blue",
    "button_green",
    "button_yellow",
    
    # Event Queue
    "EventQueue",
    "UIEvent",
    
    # Window Stack
    "Window",
    "WindowStack",
    
    # Modals
    "Modal",
    "create_alert_modal",
    "create_confirm_modal",
    "create_error_modal",
]