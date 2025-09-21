#!/usr/bin/env python3

import pygame as pg
import sys
from ..src.pygame_ui_items.elements.button_factory import *

# Inicializar pygame
pg.init()

# EJEMPLO DE USO
if __name__ == "__main__":
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    
    print("¡La librería funciona correctamente! ✅")
    
    btn_red = button_red("Eliminar", lambda: print("¡Eliminado!"), x=100, y=100)
    btn_blue = button_blue("Guardar", lambda: print("¡Guardado!"), x=100, y=160)
    btn_green = button_green("Aceptar", lambda: print("¡Aceptado!"), x=100, y=220)
    btn_yellow = button_yellow("Advertencia", lambda: print("¡Cuidado!"), x=100, y=280)
    
    btn_custom = create_button(
        "Personalizado", 
        lambda: print("¡Personalizado!"),
        x=100, 
        y=340,
        width=150,
        height=45,
        bg_color=(139, 0, 0),
        hover_bg_color=(178, 34, 34),
        text_color=(255, 255, 255),
        border_radius=70
    )
    
    buttons = [btn_red, btn_blue, btn_green, btn_yellow, btn_custom]
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            for button in buttons:
                button.handle_event(event)
        
        screen.fill((240, 240, 240))
        
        for button in buttons:
            button.draw(screen)
        
        pg.display.flip()
        clock.tick(60)
    
    pg.quit()
    sys.exit()