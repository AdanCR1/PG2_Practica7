import pygame as pg
from typing import *

class UIElement:
    """Abstract base class for UI elements"""
    def __init__(self, x: int, y: int, width: int, height: int, **kwargs):
        self._rect = pg.Rect(x, y, width, height)
        self._visible = True
        self._enabled = True
        self._styles = self._get_default_styles()
        self._apply_styles(kwargs)
    
    def _get_default_styles(self) -> Dict[str, Any]:
        return {}
    
    def _apply_styles(self, styles: Dict[str, Any]):
        for key, value in styles.items():
            if hasattr(self, f"_set_{key}"):
                getattr(self, f"_set_{key}")(value)
            elif key in self._styles:
                self._styles[key] = value
    
    def draw(self, surface: pg.Surface):
        pass
    
    def handle_event(self, event: pg.event.Event) -> bool:
        return False
    
    def update(self):
        pass
    
    @property
    def rect(self) -> pg.Rect:
        return self._rect
    
    @property
    def x(self) -> int:
        return self._rect.x
    
    @x.setter
    def x(self, value: int):
        self._rect.x = value
    
    @property
    def y(self) -> int:
        return self._rect.y
    
    @y.setter
    def y(self, value: int):
        self._rect.y = value