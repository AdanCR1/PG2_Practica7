import pygame as pg
from typing import List
from pygame_ui_items.ui_element import UIElement
from pygame_ui_items.window_stack import WindowStack

class UIManager:
    """A simple UI Manager to handle UI elements."""
    def __init__(self):
        self.elements: List[UIElement] = []
        self.window_stack = WindowStack()

    def add_element(self, element: UIElement):
        self.elements.append(element)

    def remove_element(self, element: UIElement):
        self.elements.remove(element)

    def handle_event(self, event: pg.event.Event):
        """
        Manage events. Prioritize the WindowStack.
        If the stack is not empty, ONLY it receives events.
        If empty, base elements receive events.
        """
        if not self.window_stack.is_empty():
            self.window_stack.handle_event(event)
        else:
            for element in self.elements:
                element.handle_event(event)

    def update(self):
        if not self.window_stack.is_empty():
            self.window_stack.update()
        else:
            for element in self.elements:
                element.update()

    def draw(self, surface: pg.Surface):
        for element in self.elements:
            element.draw(surface)
        self.window_stack.draw(surface)