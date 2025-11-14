import pygame as pg
import sys
from typing import Callable

# --- Importaciones de tu Librería ---
try:
    from pygame_ui_items.ui_manager import UIManager
    from pygame_ui_items.window_stack import Window
    from pygame_ui_items.modal import Modal
    from pygame_ui_items.ui_element import UIElement
    
    # --- Importar Estilo Contorno ---
    from pygame_ui_items.button_factory import (
        button_outline_green,
        button_outline_gray,
        button_outline_purple,
        button_outline_red,
        button_outline_blue # Para el modal de confirmación
    )
    
except ImportError:
    print("Error: No se pudo encontrar la librería 'pygame_ui_items'.")
    sys.exit(1)

# --- Clases de Ayuda (Panel y Label) ---
class GuiPanel(UIElement):
    def __init__(self, x, y, width, height, bg_color=(255, 255, 255), **kwargs):
        super().__init__(x, y, width, height, **kwargs)
        self._styles['bg_color'] = bg_color
    def draw(self, surface: pg.Surface):
        if self._styles['bg_color']:
            pg.draw.rect(surface, self._styles['bg_color'], self._rect)

class GuiLabel(UIElement):
    def __init__(self, x, y, text: str, font_size=24, color=(0, 0, 0), align="center"):
        self._font = pg.font.Font(None, font_size)
        self._text_surface = self._font.render(text, True, color)
        rect = self._text_surface.get_rect()
        if align == "center": rect.center = (x, y)
        elif align == "topleft": rect.topleft = (x, y)
        super().__init__(rect.x, rect.y, rect.width, rect.height)
    def draw(self, surface: pg.Surface):
        surface.blit(self._text_surface, self._rect)
# --- Fin Clases de Ayuda ---

# --- Configuración Global ---
pg.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Demo de GUI Completa - Estilo CONTORNO")
clock = pg.time.Clock()
ui_manager = UIManager()

# --- Funciones de Gestión de Estado (Stack) ---
def open_options_menu():
    ui_manager.window_stack.push(create_options_menu())
def open_game_screen():
    ui_manager.window_stack.push(create_game_screen())
def open_pause_menu():
    ui_manager.window_stack.push(create_pause_menu())
def return_to_main_menu():
    ui_manager.window_stack.pop() # Cierra pausa
    ui_manager.window_stack.pop() # Cierra juego
def close_top_window():
    ui_manager.window_stack.pop()
def open_quit_dialog():
    # Creamos un modal de confirmación personalizado para que use botones outline
    modal = Modal(SCREEN_WIDTH, SCREEN_HEIGHT, 350, 180)
    modal.add_element(GuiLabel(modal.rect.centerx, modal.rect.y + 60, "¿Seguro que quieres salir?"))
    modal.add_element(button_outline_blue("Confirmar", lambda: sys.exit(),
                        x=modal.rect.centerx - 110, y=modal.rect.y + 110))
    modal.add_element(button_outline_red("Cancelar", close_top_window,
                        x=modal.rect.centerx + 10, y=modal.rect.y + 110))
    ui_manager.window_stack.push(modal)


# --- Fábricas de Ventanas (Estados) ---

def create_main_menu() -> Window:
    menu = Window(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    # Fondo blanco para que resalten los botones outline
    menu.add_element(GuiPanel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_color=(255, 255, 255)))
    menu.add_element(GuiLabel(SCREEN_WIDTH // 2, 100, "MENÚ PRINCIPAL (CONTORNO)", font_size=50, color=(33, 37, 41)))
    
    menu.add_element(button_outline_green("Iniciar Juego", open_game_screen, 
                                          x=SCREEN_WIDTH // 2 - 100, y=250, width=200, height=50))
    menu.add_element(button_outline_purple("Opciones", open_options_menu,
                                           x=SCREEN_WIDTH // 2 - 100, y=310, width=200, height=50))
    menu.add_element(button_outline_red("Salir", open_quit_dialog,
                                        x=SCREEN_WIDTH // 2 - 100, y=370, width=200, height=50))
    return menu

def create_options_menu() -> Window:
    options = Window(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    options.add_element(GuiPanel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_color=(255, 255, 255)))
    options.add_element(GuiLabel(SCREEN_WIDTH // 2, 100, "Opciones", font_size=50, color=(33, 37, 41)))
    
    options.add_element(button_outline_gray("Volumen: [ON]", lambda: print("Click Volumen"),
                                           x=SCREEN_WIDTH // 2 - 150, y=250, width=300, height=50))
    options.add_element(button_outline_gray("Dificultad: [Fácil]", lambda: print("Click Dificultad"),
                                           x=SCREEN_WIDTH // 2 - 150, y=310, width=300, height=50))
    options.add_element(button_outline_red("Volver", close_top_window,
                                         x=SCREEN_WIDTH // 2 - 100, y=450, width=200, height=50))
    return options

def create_game_screen() -> Window:
    game = Window(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    game.add_element(GuiPanel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_color=(240, 240, 240))) # Fondo gris claro
    game.add_element(GuiLabel(SCREEN_WIDTH // 2, 300, "¡El Juego está corriendo!", font_size=40, color=(33, 37, 41)))
    game.add_element(button_outline_gray("Pausa [P]", open_pause_menu,
                                        x=SCREEN_WIDTH - 130, y=20, width=110, height=40))
    return game

def create_pause_menu() -> Modal:
    pause_menu = Modal(SCREEN_WIDTH, SCREEN_HEIGHT, 300, 280)
    pause_menu.add_element(GuiLabel(pause_menu.rect.centerx, pause_menu.rect.top + 40, "Pausa", font_size=50))
    pause_menu.add_element(button_outline_green("Reanudar", close_top_window,
                               x=pause_menu.rect.centerx - 100, y=pause_menu.rect.top + 100, width=200, height=50))
    pause_menu.add_element(button_outline_red("Menú Principal", return_to_main_menu,
                                  x=pause_menu.rect.centerx - 100, y=pause_menu.rect.top + 160, width=200, height=50))
    return pause_menu

# --- Bucle Principal ---
if __name__ == "__main__":
    ui_manager.window_stack.push(create_main_menu())
    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT: running = False
            ui_manager.handle_event(event)
        ui_manager.update()
        screen.fill((0,0,0))
        ui_manager.draw(screen)
        pg.display.flip()
        clock.tick(60)
    pg.quit()
    sys.exit()