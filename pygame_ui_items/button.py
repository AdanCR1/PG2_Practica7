import pygame as pg
from typing import Dict, Any, Callable
from pygame_ui_items.ui_element import UIElement

class Button(UIElement):
    """ Button with CSS-like style """
    
    def __init__(self, x: int, y: int, width: int, height: int, 
                 text: str = "", onclick: Callable = None, **kwargs):
        super().__init__(x, y, width, height, **kwargs)
        
        self._text = text
        self._onclick = onclick
        self._hovered = False
        self._pressed = False
        self._state = "normal"
        
        self._render_text()
    
    def _get_default_styles(self) -> Dict[str, Any]:
        return {
            "bg_color": (70, 130, 180),
            "hover_bg_color": (50, 110, 160),
            "pressed_bg_color": (30, 90, 140),
            "disabled_bg_color": (150, 150, 150),
            "text_color": (255, 255, 255),
            "hover_text_color": (255, 255, 255),
            "pressed_text_color": (255, 255, 255),
            "disabled_text_color": (100, 100, 100),
            "border_radius": 8,
            "border_width": 0,
            "border_color": (0, 0, 0),
            "font_size": 20,
            "font_name": None,
            "padding": (15, 8),
        }
    
    def _render_text(self):
        if self._styles["font_name"]:
            self._font = pg.font.SysFont(self._styles["font_name"], self._styles["font_size"])
        else:
            self._font = pg.font.Font(None, self._styles["font_size"])
        
        self._text_surface = self._font.render(self._text, True, self._styles["text_color"])
    
    def draw(self, surface: pg.Surface):
        if not self._visible:
            return
        
        """ State based color """
        if not self._enabled:
            color = self._styles["disabled_bg_color"]
        elif self._pressed:
            color = self._styles["pressed_bg_color"]
        elif self._hovered:
            color = self._styles["hover_bg_color"]
        else:
            color = self._styles["bg_color"]
        
        """ Draw button """
        if self._styles["border_radius"] > 0:
            pg.draw.rect(surface, color, self._rect, border_radius=self._styles["border_radius"])
        else:
            surface.fill(color, self._rect)
        
        """ Draw text """
        if self._text:
            padding_x, padding_y = self._styles["padding"]
            content_rect = self._rect.inflate(-padding_x * 2, -padding_y * 2)
            text_rect = self._text_surface.get_rect(center=content_rect.center)
            surface.blit(self._text_surface, text_rect)
    
    def handle_event(self, event: pg.event.Event) -> bool:
        if not self._visible or not self._enabled:
            return False
        
        if event.type == pg.MOUSEMOTION:
            self._hovered = self._rect.collidepoint(event.pos)
            return True
        
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self._hovered:
                self._pressed = True
                return True
        
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if self._pressed and self._hovered:
                self._pressed = False
                if self._onclick:
                    self._onclick()
                return True
            self._pressed = False
        
        return False

""" Classes with predefined styles """
class RedButton(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (220, 53, 69),
            "hover_bg_color": (187, 45, 59),
            "pressed_bg_color": (154, 37, 48),
            "border_radius": 10
        })
        return styles

class BlueButton(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (0, 123, 255),
            "hover_bg_color": (0, 86, 214),
            "pressed_bg_color": (0, 64, 166)
        })
        return styles

class GreenButton(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (40, 167, 69),
            "hover_bg_color": (33, 136, 56),
            "pressed_bg_color": (25, 105, 44)
        })
        return styles

class YellowButton(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (255, 193, 7),
            "hover_bg_color": (224, 168, 0),
            "pressed_bg_color": (193, 145, 0),
            "text_color": (0, 0, 0)
        })
        return styles