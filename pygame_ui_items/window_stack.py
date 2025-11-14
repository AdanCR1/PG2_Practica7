import pygame as pg
from typing import List, Optional
from pygame_ui_items.ui_element import UIElement

class Window:
    """Clase base para ventanas o modales. Es un contenedor de elementos UI."""
    def __init__(self, x: int, y: int, width: int, height: int):
        self.rect = pg.Rect(x, y, width, height)
        self.elements: List[UIElement] = []
        self._is_modal = True # Por defecto, bloquea eventos inferiores

    def add_element(self, element: UIElement):
        self.elements.append(element)
    
    def is_modal(self) -> bool:
        return self._is_modal

    def handle_event(self, event: pg.event.Event) -> bool:
        """Maneja eventos para esta ventana. Retorna True si el evento fue manejado."""
        handled = False
        for element in self.elements:
            if element.handle_event(event):
                handled = True
        
        # Si es modal, "consume" el evento incluso si no hizo nada, 
        # para evitar que pase a capas inferiores (excepto MOUSEMOTION).
        if self._is_modal and event.type != pg.MOUSEMOTION:
            return True
            
        return handled

    def update(self):
        for element in self.elements:
            element.update()

    def draw(self, surface: pg.Surface):
        for element in self.elements:
            element.draw(surface)

class WindowStack:
    """
    Implementación de una Pila (LIFO) para gestionar ventanas y modales.
    Esta es la estructura de datos principal.
    """
    def __init__(self):
        self._stack: List[Window] = []

    def push(self, window: Window):
        """Añade una ventana a la cima de la pila (push)."""
        self._stack.append(window)

    def pop(self) -> Optional[Window]:
        """Quita y retorna la ventana en la cima de la pila (pop)."""
        if not self.is_empty():
            return self._stack.pop()
        return None

    def peek(self) -> Optional[Window]:
        """Retorna la ventana en la cima de la pila sin quitarla."""
        if not self.is_empty():
            return self._stack[-1]
        return None

    def is_empty(self) -> bool:
        """Verifica si la pila está vacía."""
        return len(self._stack) == 0

    def handle_event(self, event: pg.event.Event) -> bool:
        """Pasa el evento SÓLO a la ventana en la cima de la pila."""
        top_window = self.peek()
        if top_window:
            return top_window.handle_event(event)
        return False

    def update(self):
        """Actualiza SÓLO la ventana en la cima de la pila."""
        top_window = self.peek()
        if top_window:
            top_window.update()

    def draw(self, surface: pg.Surface):
        """Dibuja SÓLO la ventana en la cima de la pila."""
        top_window = self.peek()
        if top_window:
            top_window.draw(surface)