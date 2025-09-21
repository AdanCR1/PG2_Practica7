#!/usr/bin/env python3

import pygame as pg
import sys
import os

# Añadir el directorio padre al path para importar el paquete
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pygame_ui_items.elements.button_factory import *
from pygame_ui_items.elements.button_factory import *

def main():
    # Inicializar pygame
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("PyGame UI Items - Basic Example")
    clock = pg.time.Clock()
    
    print("✨ Basic Example - PyGame UI Items")
    
    # Crear botones predefinidos en una línea
    btn_red = button_red("Eliminar", lambda: print("¡Eliminado!"), x=100, y=50)
    btn_blue = button_blue("Guardar", lambda: print("¡Guardado!"), x=100, y=120)
    btn_green = button_green("Aceptar", lambda: print("¡Aceptado!"), x=100, y=190)
    btn_yellow = button_yellow("Advertencia", lambda: print("¡Cuidado!"), x=100, y=260)
    
    # Botones con estilo Bootstrap
    btn_primary = button_primary("Primario", lambda: print("Primario!"), x=300, y=50)
    btn_success = button_success("Éxito", lambda: print("Éxito!"), x=300, y=120)
    btn_danger = button_danger("Peligro", lambda: print("Peligro!"), x=300, y=190)
    
    # Botón personalizado con CSS-like styling
    btn_custom = create_button(
        "Personalizado", 
        lambda: print("¡Personalizado!"),
        x=300, 
        y=260,
        width=180,
        height=50,
        bg_color=(139, 0, 0),          # Dark red
        hover_bg_color=(178, 34, 34),   # Firebrick
        pressed_bg_color=(165, 42, 42), # Brown
        text_color=(255, 255, 255),
        border_radius=15,
        border_width=2,
        border_color=(255, 255, 255),
        font_size=18,
        padding=(20, 12)
    )
    
    buttons = [
        btn_red, btn_blue, btn_green, btn_yellow,
        btn_primary, btn_success, btn_danger, btn_custom
    ]
    
    # Bucle principal
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time en segundos
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            # Manejar eventos para todos los botones
            for button in buttons:
                button.handle_event(event)
        
        # Actualizar (para animaciones futuras)
        for button in buttons:
            if hasattr(button, 'update'):
                button.update(dt)
        
        # Dibujar
        screen.fill((240, 240, 240))  # Fondo gris claro
        
        for button in buttons:
            button.draw(screen)
        
        # Dibujar título
        font = pg.font.Font(None, 36)
        title = font.render("PyGame UI Items - Basic Example", True, (50, 50, 50))
        screen.blit(title, (200, 10))
        
        pg.display.flip()
    
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()