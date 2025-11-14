import pygame as pg
from typing import Callable, Optional
from pygame_ui_items.window_stack import Window
from pygame_ui_items.button_factory import create_button, button_green, button_red, button_blue, button_yellow, button_gray
from pygame_ui_items.ui_element import UIElement

# Un elemento simple para el fondo del modal
class Panel(UIElement):
    def __init__(self, x, y, width, height, bg_color=(255, 255, 255), border_color=(100, 100, 100), border_width=2):
        super().__init__(x, y, width, height)
        self._styles['bg_color'] = bg_color
        self._styles['border_color'] = border_color
        self._styles['border_width'] = border_width
    
    def draw(self, surface: pg.Surface):
        pg.draw.rect(surface, self._styles['bg_color'], self._rect)
        pg.draw.rect(surface, self._styles['border_color'], self._rect, self._styles['border_width'])

# Un elemento simple para texto
class Label(UIElement):
    def __init__(self, x, y, text: str, font_size=24, color=(0, 0, 0)):
        self._font = pg.font.Font(None, font_size)
        self._text_surface = self._font.render(text, True, color)
        rect = self._text_surface.get_rect(center=(x, y))
        super().__init__(rect.x, rect.y, rect.width, rect.height)
    
    def draw(self, surface: pg.Surface):
        surface.blit(self._text_surface, self._rect)


class Modal(Window):
    """Un Modal es una Ventana que se centra en la pantalla"""
    def __init__(self, screen_width: int, screen_height: int, width: int, height: int):
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        super().__init__(x, y, width, height)
        
        # Fondo del modal
        panel = Panel(self.rect.x, self.rect.y, width, height, bg_color=(245, 245, 245))
        self.add_element(panel)

# --- Fábrica de Modales ---

def create_alert_modal(
    screen_width: int, 
    screen_height: int, 
    text: str, 
    on_close: Callable
) -> Modal:
    """Crea un modal de alerta simple con un botón 'OK'."""
    modal_width, modal_height = 300, 150
    modal = Modal(screen_width, screen_height, modal_width, modal_height)
    
    # Texto
    label = Label(modal.rect.centerx, modal.rect.y + 50, text)
    modal.add_element(label)
    
    # Botón OK
    ok_button = create_button(
        "OK", 
        onclick=on_close, 
        x=modal.rect.centerx - 50, 
        y=modal.rect.y + 90, 
        width=100
    )
    modal.add_element(ok_button)
    
    return modal

def create_confirm_modal(
    screen_width: int, 
    screen_height: int, 
    text: str, 
    on_confirm: Callable, 
    on_cancel: Callable
) -> Modal:
    """Crea un modal de confirmación con 'Confirmar' y 'Cancelar'."""
    modal_width, modal_height = 350, 180
    modal = Modal(screen_width, screen_height, modal_width, modal_height)
    
    # Texto
    label = Label(modal.rect.centerx, modal.rect.y + 60, text)
    modal.add_element(label)
    
    # Botón Confirmar
    confirm_button = button_green(
        "Confirmar", 
        onclick=on_confirm, 
        x=modal.rect.centerx - 110, 
        y=modal.rect.y + 110
    )
    modal.add_element(confirm_button)
    
    # Botón Cancelar
    cancel_button = button_red(
        "Cancelar", 
        onclick=on_cancel, 
        x=modal.rect.centerx + 10, 
        y=modal.rect.y + 110
    )
    modal.add_element(cancel_button)
    
    return modal

def create_error_modal(
    screen_width: int, 
    screen_height: int, 
    text: str, 
    on_close: Callable
) -> Modal:
    """Crea un modal de error (similar a alerta pero con botón rojo)."""
    modal_width, modal_height = 300, 150
    modal = Modal(screen_width, screen_height, modal_width, modal_height)
    
    # Texto
    label = Label(modal.rect.centerx, modal.rect.y + 50, text, color=(200, 0, 0))
    modal.add_element(label)
    
    # Botón OK
    ok_button = button_red(
        "Cerrar", 
        onclick=on_close, 
        x=modal.rect.centerx - 50, 
        y=modal.rect.y + 90, 
        width=100
    )
    modal.add_element(ok_button)
    
    return modal

def create_success_modal(
    screen_width: int, 
    screen_height: int, 
    text: str, 
    on_close: Callable
) -> Modal:
    """Crea un modal de éxito con botón verde y texto verde."""
    modal_width, modal_height = 320, 160
    modal = Modal(screen_width, screen_height, modal_width, modal_height)
    
    # Símbolo de éxito
    success_label = Label(modal.rect.centerx, modal.rect.y + 30, "✓ ÉXITO", font_size=20, color=(40, 167, 69))
    modal.add_element(success_label)
    
    # Texto
    label = Label(modal.rect.centerx, modal.rect.y + 60, text, font_size=18, color=(25, 105, 44))
    modal.add_element(label)
    
    # Botón OK
    ok_button = button_green(
        "Continuar", 
        onclick=on_close, 
        x=modal.rect.centerx - 60, 
        y=modal.rect.y + 100, 
        width=120
    )
    modal.add_element(ok_button)
    
    return modal

def create_warning_modal(
    screen_width: int, 
    screen_height: int, 
    text: str, 
    on_proceed: Callable,
    on_cancel: Callable
) -> Modal:
    """Crea un modal de advertencia con botones Proceder/Cancelar."""
    modal_width, modal_height = 380, 180
    modal = Modal(screen_width, screen_height, modal_width, modal_height)
    
    # Símbolo de advertencia
    warning_label = Label(modal.rect.centerx, modal.rect.y + 30, "⚠ ADVERTENCIA", font_size=20, color=(255, 193, 7))
    modal.add_element(warning_label)
    
    # Texto
    label = Label(modal.rect.centerx, modal.rect.y + 60, text, font_size=16, color=(193, 145, 0))
    modal.add_element(label)
    
    # Botón Proceder
    proceed_button = button_yellow(
        "Proceder", 
        onclick=on_proceed, 
        x=modal.rect.centerx - 120, 
        y=modal.rect.y + 120
    )
    modal.add_element(proceed_button)
    
    # Botón Cancelar
    cancel_button = button_gray(
        "Cancelar", 
        onclick=on_cancel, 
        x=modal.rect.centerx + 20, 
        y=modal.rect.y + 120
    )
    modal.add_element(cancel_button)
    
    return modal

def create_info_modal(
    screen_width: int, 
    screen_height: int, 
    text: str, 
    on_close: Callable
) -> Modal:
    """Crea un modal de información con botón azul y texto azul."""
    modal_width, modal_height = 340, 160
    modal = Modal(screen_width, screen_height, modal_width, modal_height)
    
    # Símbolo de información
    info_label = Label(modal.rect.centerx, modal.rect.y + 30, "ℹ INFORMACIÓN", font_size=20, color=(0, 123, 255))
    modal.add_element(info_label)
    
    # Texto
    label = Label(modal.rect.centerx, modal.rect.y + 60, text, font_size=18, color=(0, 86, 214))
    modal.add_element(label)
    
    # Botón OK
    ok_button = button_blue(
        "Entendido", 
        onclick=on_close, 
        x=modal.rect.centerx - 60, 
        y=modal.rect.y + 100, 
        width=120
    )
    modal.add_element(ok_button)
    
    return modal

# Elemento simple para input de texto
class TextInput(UIElement):
    def __init__(self, x, y, width, height, placeholder="", **kwargs):
        super().__init__(x, y, width, height, **kwargs)
        self._text = ""
        self._placeholder = placeholder
        self._active = False
        self._cursor_visible = True
        self._cursor_timer = 0
        self._font = pg.font.Font(None, 24)
        self._styles.update({
            "bg_color": (255, 255, 255),
            "border_color": (200, 200, 200),
            "active_border_color": (0, 123, 255),
            "text_color": (0, 0, 0),
            "placeholder_color": (150, 150, 150),
            "border_width": 2,
            "border_radius": 5,
            "padding": (10, 8)
        })
    
    def handle_event(self, event: pg.event.Event) -> bool:
        if not self._visible or not self._enabled:
            return False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            self._active = self._rect.collidepoint(event.pos)
            return self._active
        
        elif event.type == pg.KEYDOWN and self._active:
            if event.key == pg.K_BACKSPACE:
                self._text = self._text[:-1]
            elif event.key == pg.K_RETURN:
                self._active = False
            else:
                self._text += event.unicode
            return True
        
        return False
    
    def update(self):
        self._cursor_timer += 1
        if self._cursor_timer > 30:
            self._cursor_visible = not self._cursor_visible
            self._cursor_timer = 0
    
    def draw(self, surface: pg.Surface):
        if not self._visible:
            return
        
        # Fondo
        pg.draw.rect(surface, self._styles["bg_color"], self._rect, border_radius=self._styles["border_radius"])
        
        # Borde
        border_color = self._styles["active_border_color"] if self._active else self._styles["border_color"]
        pg.draw.rect(surface, border_color, self._rect, border_radius=self._styles["border_radius"], width=self._styles["border_width"])
        
        # Texto
        display_text = self._text if self._text else self._placeholder
        text_color = self._styles["text_color"] if self._text else self._styles["placeholder_color"]
        
        if display_text:
            text_surface = self._font.render(display_text, True, text_color)
            padding_x, padding_y = self._styles["padding"]
            text_rect = text_surface.get_rect()
            text_rect.x = self._rect.x + padding_x
            text_rect.centery = self._rect.centery
            surface.blit(text_surface, text_rect)
        
        # Cursor
        if self._active and self._cursor_visible and self._text:
            text_width = self._font.size(self._text)[0]
            padding_x, _ = self._styles["padding"]
            cursor_x = self._rect.x + padding_x + text_width
            cursor_y1 = self._rect.y + 8
            cursor_y2 = self._rect.bottom - 8
            pg.draw.line(surface, self._styles["text_color"], (cursor_x, cursor_y1), (cursor_x, cursor_y2), 2)
    
    def get_text(self) -> str:
        return self._text
    
    def set_text(self, text: str):
        self._text = text

def create_input_modal(
    screen_width: int, 
    screen_height: int, 
    title: str,
    placeholder: str,
    on_submit: Callable,
    on_cancel: Callable
) -> Modal:
    """Crea un modal con campo de entrada de texto."""
    modal_width, modal_height = 400, 200
    modal = Modal(screen_width, screen_height, modal_width, modal_height)
    
    # Título
    title_label = Label(modal.rect.centerx, modal.rect.y + 30, title, font_size=20, color=(0, 0, 0))
    modal.add_element(title_label)
    
    # Campo de entrada
    text_input = TextInput(
        modal.rect.x + 20, 
        modal.rect.y + 60, 
        modal_width - 40, 
        35, 
        placeholder=placeholder
    )
    modal.add_element(text_input)
    
    # Función que captura el texto y llama al callback
    def submit_with_text():
        on_submit(text_input.get_text())
    
    # Botón Enviar
    submit_button = button_blue(
        "Enviar", 
        onclick=submit_with_text, 
        x=modal.rect.centerx - 110, 
        y=modal.rect.y + 130
    )
    modal.add_element(submit_button)
    
    # Botón Cancelar
    cancel_button = button_gray(
        "Cancelar", 
        onclick=on_cancel, 
        x=modal.rect.centerx + 10, 
        y=modal.rect.y + 130
    )
    modal.add_element(cancel_button)
    
    return modal