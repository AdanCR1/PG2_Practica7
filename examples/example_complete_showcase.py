import pygame as pg
import sys
from typing import Callable

from pygame_ui_items.ui_manager import UIManager
from pygame_ui_items.event_queue import EventQueue, UIEvent
from pygame_ui_items.window_stack import Window
from pygame_ui_items.ui_element import UIElement

from pygame_ui_items.button_factory import *

from pygame_ui_items.modal import *

# Clases auxiliares para UI
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

class NotificationPanel(UIElement):
    """Panel para mostrar notificaciones del EventQueue"""
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.notifications = []
        self._font = pg.font.Font(None, 20)
    
    def add_notification(self, text: str, color=(0, 0, 0)):
        self.notifications.append({"text": text, "color": color, "timer": 180})  # 3 segundos a 60fps
    
    def update(self):
        self.notifications = [n for n in self.notifications if n["timer"] > 0]
        for notification in self.notifications:
            notification["timer"] -= 1
    
    def draw(self, surface: pg.Surface):
        if self.notifications:
            s = pg.Surface((self._rect.width, self._rect.height), pg.SRCALPHA)
            pg.draw.rect(s, (0, 0, 0, 100), s.get_rect(), border_radius=10)
            surface.blit(s, self._rect)
        
        y_offset = 10
        for notification in self.notifications:
            alpha = min(255, notification["timer"] * 2)  # Fade out
            color = (*notification["color"], alpha)
            text_surface = self._font.render(notification["text"], True, notification["color"])
            surface.blit(text_surface, (self._rect.x + 10, self._rect.y + y_offset))
            y_offset += 25

# Configuración global
pg.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("🎨 pygame_ui_items v0.0.2 - Showcase Completo")
clock = pg.time.Clock()

# Inicializar sistemas
ui_manager = UIManager()
event_queue = EventQueue()
notification_panel = NotificationPanel(SCREEN_WIDTH - 320, 10, 300, 200)

# --- Funciones de Callback ---
def show_notification(message: str, color=(0, 100, 0)):
    """Añade notificación usando EventQueue"""
    notification_panel.add_notification(message, color)

def close_top_modal():
    ui_manager.window_stack.pop()

def demo_callback(style_name: str, color_name: str):
    """Callback genérico para botones de demostración"""
    def callback():
        event_queue.add_event(
            callback=lambda: show_notification(f"✓ {style_name} {color_name}", (0, 150, 0)),
            priority=EventQueue.NORMAL,
            event_type="button_click",
            delay=0.0
        )
    return callback

def open_alert_modal():
    modal = create_alert_modal(SCREEN_WIDTH, SCREEN_HEIGHT, "¡Esta es una alerta básica!", close_top_modal)
    ui_manager.window_stack.push(modal)

def open_confirm_modal():
    modal = create_confirm_modal(
        SCREEN_WIDTH, SCREEN_HEIGHT, "¿Confirmas esta acción?",
        on_confirm=lambda: (show_notification("✓ Confirmado", (0, 150, 0)), close_top_modal()),
        on_cancel=lambda: (show_notification("✗ Cancelado", (150, 0, 0)), close_top_modal())
    )
    ui_manager.window_stack.push(modal)

def open_error_modal():
    modal = create_error_modal(SCREEN_WIDTH, SCREEN_HEIGHT, "¡Ha ocurrido un error!", close_top_modal)
    ui_manager.window_stack.push(modal)

def open_success_modal():
    modal = create_success_modal(SCREEN_WIDTH, SCREEN_HEIGHT, "¡Operación completada exitosamente!", close_top_modal)
    ui_manager.window_stack.push(modal)

def open_warning_modal():
    modal = create_warning_modal(
        SCREEN_WIDTH, SCREEN_HEIGHT, "Esta acción no se puede deshacer",
        on_proceed=lambda: (show_notification("⚠ Procediendo...", (200, 150, 0)), close_top_modal()),
        on_cancel=close_top_modal
    )
    ui_manager.window_stack.push(modal)

def open_info_modal():
    modal = create_info_modal(SCREEN_WIDTH, SCREEN_HEIGHT, "Información importante sobre el sistema", close_top_modal)
    ui_manager.window_stack.push(modal)

def open_input_modal():
    def handle_input(text):
        show_notification(f"📝 Texto ingresado: '{text}'", (0, 0, 150))
        close_top_modal()
    
    modal = create_input_modal(
        SCREEN_WIDTH, SCREEN_HEIGHT, "Ingresa tu nombre:",
        "Escribe aquí...", handle_input, close_top_modal
    )
    ui_manager.window_stack.push(modal)

def create_showcase_window() -> Window:
    window = Window(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    window.add_element(GuiPanel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_color=(240, 245, 250)))
    
    window.add_element(GuiLabel(SCREEN_WIDTH // 2, 30, "🎨 pygame_ui_items v0.0.2 - Showcase Completo", font_size=32, color=(30, 30, 30)))
    
    window.add_element(GuiLabel(SCREEN_WIDTH // 2, 60, "4 Estilos × 12 Colores = 48 Botones + EventQueue + 7 Modales", font_size=18, color=(100, 100, 100)))
    
    # --- SECCIÓN 1: BOTONES SÓLIDOS ---
    y_start = 120
    window.add_element(GuiLabel(150, y_start, "ESTILO 1: SÓLIDO", font_size=20, color=(50, 50, 50)))
    
    solid_buttons = [
        (button_gray, "Gray"), (button_black, "Black"), (button_brown, "Brown"),
        (button_orange, "Orange"), (button_red, "Red"), (button_pink, "Pink"),
        (button_yellow, "Yellow"), (button_lime, "Lime"), (button_green, "Green"),
        (button_light_blue, "Light Blue"), (button_blue, "Blue"), (button_purple, "Purple")
    ]
    
    for i, (btn_func, color_name) in enumerate(solid_buttons):
        x = 50 + (i % 6) * 180
        y = y_start + 30 + (i // 6) * 50
        btn = btn_func(color_name, demo_callback("Sólido", color_name), x=x, y=y, width=160, height=35)
        window.add_element(btn)
    
    # --- SECCIÓN 2: BOTONES CONTORNO ---
    y_start = 240
    window.add_element(GuiLabel(150, y_start, "ESTILO 2: CONTORNO", font_size=20, color=(50, 50, 50)))
    
    outline_buttons = [
        (button_outline_gray, "Gray"), (button_outline_black, "Black"), (button_outline_brown, "Brown"),
        (button_outline_orange, "Orange"), (button_outline_red, "Red"), (button_outline_pink, "Pink"),
        (button_outline_yellow, "Yellow"), (button_outline_lime, "Lime"), (button_outline_green, "Green"),
        (button_outline_light_blue, "Light Blue"), (button_outline_blue, "Blue"), (button_outline_purple, "Purple")
    ]
    
    for i, (btn_func, color_name) in enumerate(outline_buttons):
        x = 50 + (i % 6) * 180
        y = y_start + 30 + (i // 6) * 50
        btn = btn_func(color_name, demo_callback("Contorno", color_name), x=x, y=y, width=160, height=35)
        window.add_element(btn)
    
    # --- SECCIÓN 3: BOTONES GRADIENTE (NUEVO) ---
    y_start = 360
    window.add_element(GuiLabel(150, y_start, "ESTILO 3: GRADIENTE ✨", font_size=20, color=(50, 50, 50)))
    
    gradient_buttons = [
        (button_gradient_gray, "Gray"), (button_gradient_black, "Black"), (button_gradient_brown, "Brown"),
        (button_gradient_orange, "Orange"), (button_gradient_red, "Red"), (button_gradient_pink, "Pink"),
        (button_gradient_yellow, "Yellow"), (button_gradient_lime, "Lime"), (button_gradient_green, "Green"),
        (button_gradient_light_blue, "Light Blue"), (button_gradient_blue, "Blue"), (button_gradient_purple, "Purple")
    ]
    
    for i, (btn_func, color_name) in enumerate(gradient_buttons):
        x = 50 + (i % 6) * 180
        y = y_start + 30 + (i // 6) * 50
        btn = btn_func(color_name, demo_callback("Gradiente", color_name), x=x, y=y, width=160, height=35)
        window.add_element(btn)
    
    # --- SECCIÓN 4: BOTONES NEUMÓRFICOS (NUEVO) ---
    y_start = 480
    window.add_element(GuiLabel(150, y_start, "ESTILO 4: NEUMÓRFICO 🔮", font_size=20, color=(50, 50, 50)))
    
    neumorphic_buttons = [
        (button_neumorphic_gray, "Gray"), (button_neumorphic_black, "Black"), (button_neumorphic_brown, "Brown"),
        (button_neumorphic_orange, "Orange"), (button_neumorphic_red, "Red"), (button_neumorphic_pink, "Pink"),
        (button_neumorphic_yellow, "Yellow"), (button_neumorphic_lime, "Lime"), (button_neumorphic_green, "Green"),
        (button_neumorphic_light_blue, "Light Blue"), (button_neumorphic_blue, "Blue"), (button_neumorphic_purple, "Purple")
    ]
    
    for i, (btn_func, color_name) in enumerate(neumorphic_buttons):
        x = 50 + (i % 6) * 180
        y = y_start + 30 + (i // 6) * 50
        btn = btn_func(color_name, demo_callback("Neumórfico", color_name), x=x, y=y, width=160, height=35)
        window.add_element(btn)
    
    # --- SECCIÓN 5: MODALES ---
    y_start = 580
    window.add_element(GuiLabel(SCREEN_WIDTH // 2, y_start, "🔔 PLANTILLAS DE MODALES (Teclas 1-7)", font_size=20, color=(50, 50, 50)))
    
    modal_buttons = [
        ("1️⃣ Alerta", open_alert_modal),
        ("2️⃣ Confirmación", open_confirm_modal),
        ("3️⃣ Error", open_error_modal),
        ("4️⃣ Éxito ✨", open_success_modal),
        ("5️⃣ Advertencia ✨", open_warning_modal),
        ("6️⃣ Información ✨", open_info_modal),
        ("7️⃣ Input ✨", open_input_modal),
    ]
    
    for i, (text, callback) in enumerate(modal_buttons):
        x = 50 + i * 160
        y = y_start + 30
        btn = button_blue(text, callback, x=x, y=y, width=150, height=40)
        window.add_element(btn)
    
    # --- INFORMACIÓN ADICIONAL ---
    window.add_element(GuiLabel(SCREEN_WIDTH // 2, 680, "EventQueue procesa notificaciones con prioridades", font_size=16, color=(100, 100, 100)))
    window.add_element(GuiLabel(SCREEN_WIDTH // 2, 700, "WindowStack gestiona modales como una pila (LIFO)", font_size=16, color=(100, 100, 100)))
    window.add_element(GuiLabel(SCREEN_WIDTH // 2, 720, "Presiona ESC para cerrar modal | Q para salir", font_size=16, color=(100, 100, 100)))
    
    return window

# --- Bucle Principal ---
if __name__ == "__main__":
    ui_manager.window_stack.push(create_showcase_window())
    
    event_queue.add_event(
        callback=lambda: show_notification("🎉 ¡Bienvenido al Showcase!", (0, 100, 200)),
        priority=EventQueue.HIGH,
        event_type="welcome",
        delay=0.5
    )
    
    running = True
    while running:
        events = pg.event.get()
        
        for event in events:
            if event.type == pg.QUIT:
                running = False
            
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_1: open_alert_modal()
                elif event.key == pg.K_2: open_confirm_modal()
                elif event.key == pg.K_3: open_error_modal()
                elif event.key == pg.K_4: open_success_modal()
                elif event.key == pg.K_5: open_warning_modal()
                elif event.key == pg.K_6: open_info_modal()
                elif event.key == pg.K_7: open_input_modal()
                elif event.key == pg.K_ESCAPE and not ui_manager.window_stack.is_empty():
                    if len(ui_manager.window_stack._stack) > 1:
                        close_top_modal()
                elif event.key == pg.K_q:
                    running = False
            
            ui_manager.handle_event(event)
        
        event_queue.process_events()
        
        ui_manager.update()
        notification_panel.update()
        
        screen.fill((240, 245, 250))
        ui_manager.draw(screen)
        notification_panel.draw(screen)
        
        stats = event_queue.get_stats()
        stats_text = f"EventQueue: {stats['pending_events']} pendientes | {stats['total_processed']} procesados"
        font = pg.font.Font(None, 20)
        stats_surface = font.render(stats_text, True, (100, 100, 100))
        screen.blit(stats_surface, (10, SCREEN_HEIGHT - 25))
        
        pg.display.flip()
        clock.tick(60)
    
    pg.quit()
    sys.exit()
