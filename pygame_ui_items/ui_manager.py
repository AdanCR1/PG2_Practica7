import pygame as pg
from typing import List
from pygame_ui_items.ui_element import UIElement

class UIManager:
    """A simple UI Manager to handle UI elements."""
    def __init__(self):
        self.elements: List[UIElement] = []

    def add_element(self, element: UIElement):
        self.elements.append(element)

    def remove_element(self, element: UIElement):
        self.elements.remove(element)

    def handle_event(self, event: pg.event.Event):
        for element in self.elements:
            element.handle_event(event)

    def update(self):
        for element in self.elements:
            element.update()

    def draw(self, surface: pg.Surface):
        for element in self.elements:
            element.draw(surface)