import pygame as pg
import sys
from pygame_ui_items.button_factory import (
    button_gray, button_black, button_brown, button_orange, button_red, button_pink,
    button_yellow, button_lime, button_green, button_light_blue, button_blue, button_purple
)

pg.init()

if __name__ == "__main__":
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Estilo de Botones: Sólido (Normal)")
    clock = pg.time.Clock()

    # Nombres de los botones en el orden solicitado
    button_factories = [
        (button_gray, "Gris"), (button_black, "Negro"), (button_brown, "Café"),
        (button_orange, "Naranja"), (button_red, "Rojo"), (button_pink, "Rosado"),
        (button_yellow, "Amarillo"), (button_lime, "Verde Lechuga"), (button_green, "Verde"),
        (button_light_blue, "Celeste"), (button_blue, "Azul"), (button_purple, "Morado")
    ]

    buttons = []
    x_col1, x_col2 = 50, 200
    y_start, y_step = 50, 60
    
    for i, (factory, text) in enumerate(button_factories):
        x = x_col1 if i < 6 else x_col2
        y = y_start + (i % 6) * y_step
        
        # El botón de texto negro necesita texto blanco
        if text == "Negro":
            btn = factory(text, lambda t=text: print(f"Click {t}"), x=x, y=y)
        # Los botones claros necesitan texto oscuro
        elif text in ["Amarillo", "Verde Lechuga", "Celeste"]:
            btn = factory(text, lambda t=text: print(f"Click {t}"), x=x, y=y, text_color=(0,0,0))
        else:
            btn = factory(text, lambda t=text: print(f"Click {t}"), x=x, y=y)
        
        buttons.append(btn)


    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            for button in buttons:
                button.handle_event(event)

        screen.fill((0,0,0))
        for button in buttons:
            button.draw(screen)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
    sys.exit()