#!/usr/bin/env python3

import pygame as pg
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pygame_ui_items import create_button, button_primary
from pygame_ui_items.styles import DarkTheme, LightTheme, ModernTheme

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("PyGame UI Items - Theme Example")
    clock = pg.time.Clock()
    
    print("🎨 Theme Example - PyGame UI Items")
    
    # Crear temas
    dark_theme = DarkTheme()
    light_theme = LightTheme()
    modern_theme = ModernTheme()
    
    # Botones con diferentes temas
    btn_dark = create_button("Dark Theme", lambda: print("Dark!"), x=100, y=100)
    btn_light = create_button("Light Theme", lambda: print("Light!"), x=100, y=180)
    btn_modern = create_button("Modern Theme", lambda: print("Modern!"), x=100, y=260)
    
    # Aplicar temas
    dark_theme.apply_to_element(btn_dark)
    light_theme.apply_to_element(btn_light)
    modern_theme.apply_to_element(btn_modern)
    
    # Botones predefinidos que ya usan temas incorporados
    btn_primary1 = button_primary("Primary", lambda: print("Primary!"), x=300, y=100)
    btn_primary2 = button_primary("Primary", lambda: print("Primary!"), x=300, y=180)
    btn_primary3 = button_primary("Primary", lambda: print("Primary!"), x=300, y=260)
    
    buttons = [btn_dark, btn_light, btn_modern, btn_primary1, btn_primary2, btn_primary3]
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            for button in buttons:
                button.handle_event(event)
        
        screen.fill((200, 200, 200))
        
        # Dibujar áreas de fondo para los temas
        pg.draw.rect(screen, (40, 40, 40), (50, 80, 200, 100))
        pg.draw.rect(screen, (230, 230, 230), (50, 160, 200, 100))
        pg.draw.rect(screen, (240, 240, 240), (50, 240, 200, 100))
        
        for button in buttons:
            button.draw(screen)
        
        # Etiquetas de temas
        font = pg.font.Font(None, 24)
        labels = [
            ("Dark Theme", 60, 80),
            ("Light Theme", 60, 160), 
            ("Modern Theme", 60, 240),
            ("Predefined Styles", 320, 80)
        ]
        
        for text, x, y in labels:
            label = font.render(text, True, (50, 50, 50))
            screen.blit(label, (x, y - 30))
        
        pg.display.flip()
        clock.tick(60)
    
    pg.quit()

if __name__ == "__main__":
    main()