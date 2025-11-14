import pygame as pg
import sys
from pygame_ui_items.button_factory import *

pg.init()

if __name__ == "__main__":
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Estilo de Botones: Contorno (Outline)")
    clock = pg.time.Clock()

    button_factories = [
        (button_outline_gray, "Gris"), (button_outline_black, "Negro"), (button_outline_brown, "Café"),
        (button_outline_orange, "Naranja"), (button_outline_red, "Rojo"), (button_outline_pink, "Rosado"),
        (button_outline_yellow, "Amarillo"), (button_outline_lime, "Verde Lechuga"), (button_outline_green, "Verde"),
        (button_outline_light_blue, "Celeste"), (button_outline_blue, "Azul"), (button_outline_purple, "Morado")
    ]

    buttons = []
    x_col1, x_col2 = 50, 200
    y_start, y_step = 50, 60
    
    for i, (factory, text) in enumerate(button_factories):
        x = x_col1 if i < 6 else x_col2
        y = y_start + (i % 6) * y_step
        
        btn = factory(text, lambda t=text: print(f"Click {t}"), x=x, y=y)
        buttons.append(btn)


    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            for button in buttons:
                button.handle_event(event)

        screen.fill((0,0,0)) # Fondo blanco para que el estilo outline resalte
        for button in buttons:
            button.draw(screen)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
    sys.exit()