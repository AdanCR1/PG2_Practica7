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
        
        """ 1. Determinar color de fondo y texto """
        if not self._enabled:
            bg_color = self._styles["disabled_bg_color"]
            text_color = self._styles["disabled_text_color"]
        elif self._pressed:
            bg_color = self._styles["pressed_bg_color"]
            text_color = self._styles["pressed_text_color"]
        elif self._hovered:
            bg_color = self._styles["hover_bg_color"]
            text_color = self._styles["hover_text_color"]
        else:
            bg_color = self._styles["bg_color"]
            text_color = self._styles["text_color"]
        
        """ 2. Dibujar el fondo del botón """
        if bg_color:
            pg.draw.rect(surface, bg_color, self._rect, border_radius=self._styles["border_radius"])
        
        """ 3. Dibujar el borde (si existe) """
        border_width = self._styles.get("border_width", 0)
        if border_width > 0:
            border_color = self._styles.get("border_color", (0,0,0))
            
            if self._hovered and self._styles.get("hover_border_color"):
                border_color = self._styles["hover_border_color"]
            elif self._pressed and self._styles.get("pressed_border_color"):
                 border_color = self._styles["pressed_border_color"]
            
            pg.draw.rect(surface, border_color, self._rect, 
                         border_radius=self._styles["border_radius"], 
                         width=border_width)

        """ 4. Dibujar el texto """
        if self._text:
            if not hasattr(self, "_last_text_color") or self._last_text_color != text_color:
                self._text_surface = self._font.render(self._text, True, text_color)
                self._last_text_color = text_color
            
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
    
""" ---------------------------- """
""" STYLE 1: SOLID COLOR BUTTONS """
""" ---------------------------- """

class ButtonRed(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (220, 53, 69),
            "hover_bg_color": (187, 45, 59),
            "pressed_bg_color": (154, 37, 48),
        })
        return styles

class ButtonBlue(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (0, 123, 255),
            "hover_bg_color": (0, 86, 214),
            "pressed_bg_color": (0, 64, 166)
        })
        return styles

class ButtonGreen(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (40, 167, 69),
            "hover_bg_color": (33, 136, 56),
            "pressed_bg_color": (25, 105, 44)
        })
        return styles

class ButtonYellow(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (255, 193, 7),
            "hover_bg_color": (224, 168, 0),
            "pressed_bg_color": (193, 145, 0),
            "text_color": (0, 0, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonGray(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (108, 117, 125),
            "hover_bg_color": (73, 80, 87),
            "pressed_bg_color": (52, 58, 64),
        })
        return styles

class ButtonBlack(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (33, 37, 41),
            "hover_bg_color": (0, 0, 0),
            "pressed_bg_color": (0, 0, 0),
        })
        return styles

class ButtonBrown(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (115, 74, 47),
            "hover_bg_color": (87, 56, 35),
            "pressed_bg_color": (64, 41, 26),
        })
        return styles

class ButtonOrange(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (253, 126, 20),
            "hover_bg_color": (220, 108, 11),
            "pressed_bg_color": (198, 97, 10),
        })
        return styles

class ButtonPink(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (214, 51, 132),
            "hover_bg_color": (186, 44, 115),
            "pressed_bg_color": (158, 37, 98),
        })
        return styles

class ButtonLime(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (132, 204, 22),
            "hover_bg_color": (107, 166, 18),
            "pressed_bg_color": (89, 138, 15),
            "text_color": (0, 0, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonLightBlue(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (13, 202, 240),
            "hover_bg_color": (11, 172, 204),
            "pressed_bg_color": (9, 149, 176),
            "text_color": (0, 0, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonPurple(Button):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (111, 66, 193),
            "hover_bg_color": (94, 56, 164),
            "pressed_bg_color": (79, 47, 138),
        })
        return styles


""" ------------------------- """
""" STYLE 2: OUTLINE BUTTONS  """
""" ------------------------- """

class ButtonOutlineBase(Button):
    """
    Base class for 'outline' buttons.
    Transparent background, text and colored border.
    On hover, it is inverted: colored background, white text.
    """
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": None,
            "hover_bg_color": (108, 117, 125),
            "pressed_bg_color": (86, 94, 100),
            "text_color": (33, 37, 41),
            "hover_text_color": (255, 255, 255),
            "pressed_text_color": (255, 255, 255),
            "border_width": 2,
            "border_color": (108, 117, 125),
            "hover_border_color": None,
            "pressed_border_color": None,
            "border_radius": 5
        })
        return styles

class ButtonOutlineGray(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (108, 117, 125)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (73, 80, 87)
        })
        return styles

class ButtonOutlineBlack(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (33, 37, 41)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (0, 0, 0)
        })
        return styles

class ButtonOutlineBrown(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (115, 74, 47)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (87, 56, 35)
        })
        return styles

class ButtonOutlineOrange(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (253, 126, 20)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (220, 108, 11)
        })
        return styles

class ButtonOutlineRed(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (220, 53, 69)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (187, 45, 59)
        })
        return styles

class ButtonOutlinePink(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (214, 51, 132)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (186, 44, 115)
        })
        return styles

class ButtonOutlineYellow(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (255, 193, 7)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (224, 168, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonOutlineLime(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (132, 204, 22)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (107, 166, 18),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonOutlineGreen(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (40, 167, 69)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (33, 136, 56)
        })
        return styles

class ButtonOutlineLightBlue(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (13, 202, 240)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (11, 172, 204),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonOutlineBlue(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (0, 123, 255)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (0, 86, 214)
        })
        return styles

class ButtonOutlinePurple(ButtonOutlineBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        color = (111, 66, 193)
        styles.update({
            "text_color": color, "border_color": color,
            "hover_bg_color": color, "pressed_bg_color": (94, 56, 164)
        })
        return styles


""" ------------------------- """
""" STYLE 3: GRADIENT BUTTONS """
""" ------------------------- """

class ButtonGradientBase(Button):
    """
    Base class for 'gradient' buttons.
    Simulates gradient effect with layered rectangles.
    """
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (108, 117, 125),
            "bg_color_secondary": (73, 80, 87),  # Color secundario para gradiente
            "hover_bg_color": (73, 80, 87),
            "hover_bg_color_secondary": (52, 58, 64),
            "pressed_bg_color": (52, 58, 64),
            "pressed_bg_color_secondary": (33, 37, 41),
            "border_radius": 10,
            "border_width": 0,
        })
        return styles
    
    def draw(self, surface: pg.Surface):
        if not self._visible:
            return
        
        # Determinar colores según estado
        if not self._enabled:
            color1 = self._styles["disabled_bg_color"]
            color2 = self._styles["disabled_bg_color"]
            text_color = self._styles["disabled_text_color"]
        elif self._pressed:
            color1 = self._styles["pressed_bg_color"]
            color2 = self._styles.get("pressed_bg_color_secondary", color1)
            text_color = self._styles["pressed_text_color"]
        elif self._hovered:
            color1 = self._styles["hover_bg_color"]
            color2 = self._styles.get("hover_bg_color_secondary", color1)
            text_color = self._styles["hover_text_color"]
        else:
            color1 = self._styles["bg_color"]
            color2 = self._styles.get("bg_color_secondary", color1)
            text_color = self._styles["text_color"]
        
        # Simular gradiente vertical con rectángulos
        steps = 5
        step_height = self._rect.height // steps
        for i in range(steps):
            ratio = i / (steps - 1)
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            
            rect = pg.Rect(
                self._rect.x,
                self._rect.y + i * step_height,
                self._rect.width,
                step_height + 1
            )
            pg.draw.rect(surface, (r, g, b), rect)
        
        # Overlay con border radius
        pg.draw.rect(surface, color1, self._rect, border_radius=self._styles["border_radius"], width=0)
        
        # Dibujar gradiente final
        for i in range(steps):
            ratio = i / (steps - 1)
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            
            y_pos = self._rect.y + i * step_height
            rect = pg.Rect(self._rect.x, y_pos, self._rect.width, step_height + 1)
            
            if i == 0:
                # Primera franja con border radius superior
                s = pg.Surface((self._rect.width, step_height + 1), pg.SRCALPHA)
                pg.draw.rect(s, (r, g, b, 255), s.get_rect(), border_top_left_radius=self._styles["border_radius"], border_top_right_radius=self._styles["border_radius"])
                surface.blit(s, (self._rect.x, y_pos))
            elif i == steps - 1:
                # Última franja con border radius inferior
                s = pg.Surface((self._rect.width, step_height + 1), pg.SRCALPHA)
                pg.draw.rect(s, (r, g, b, 255), s.get_rect(), border_bottom_left_radius=self._styles["border_radius"], border_bottom_right_radius=self._styles["border_radius"])
                surface.blit(s, (self._rect.x, y_pos))
            else:
                pg.draw.rect(surface, (r, g, b), rect)
        
        # Dibujar texto
        if self._text:
            if not hasattr(self, "_last_text_color") or self._last_text_color != text_color:
                self._text_surface = self._font.render(self._text, True, text_color)
                self._last_text_color = text_color
            
            padding_x, padding_y = self._styles["padding"]
            content_rect = self._rect.inflate(-padding_x * 2, -padding_y * 2)
            text_rect = self._text_surface.get_rect(center=content_rect.center)
            surface.blit(self._text_surface, text_rect)

class ButtonGradientGray(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (108, 117, 125),
            "bg_color_secondary": (73, 80, 87),
            "hover_bg_color": (73, 80, 87),
            "hover_bg_color_secondary": (52, 58, 64),
            "pressed_bg_color": (52, 58, 64),
            "pressed_bg_color_secondary": (33, 37, 41),
        })
        return styles

class ButtonGradientBlack(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (52, 58, 64),
            "bg_color_secondary": (33, 37, 41),
            "hover_bg_color": (33, 37, 41),
            "hover_bg_color_secondary": (0, 0, 0),
            "pressed_bg_color": (0, 0, 0),
            "pressed_bg_color_secondary": (0, 0, 0),
        })
        return styles

class ButtonGradientBrown(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (115, 74, 47),
            "bg_color_secondary": (87, 56, 35),
            "hover_bg_color": (87, 56, 35),
            "hover_bg_color_secondary": (64, 41, 26),
            "pressed_bg_color": (64, 41, 26),
            "pressed_bg_color_secondary": (50, 32, 20),
        })
        return styles

class ButtonGradientOrange(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (253, 126, 20),
            "bg_color_secondary": (220, 108, 11),
            "hover_bg_color": (220, 108, 11),
            "hover_bg_color_secondary": (198, 97, 10),
            "pressed_bg_color": (198, 97, 10),
            "pressed_bg_color_secondary": (170, 83, 8),
        })
        return styles

class ButtonGradientRed(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (220, 53, 69),
            "bg_color_secondary": (187, 45, 59),
            "hover_bg_color": (187, 45, 59),
            "hover_bg_color_secondary": (154, 37, 48),
            "pressed_bg_color": (154, 37, 48),
            "pressed_bg_color_secondary": (120, 29, 37),
        })
        return styles

class ButtonGradientPink(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (214, 51, 132),
            "bg_color_secondary": (186, 44, 115),
            "hover_bg_color": (186, 44, 115),
            "hover_bg_color_secondary": (158, 37, 98),
            "pressed_bg_color": (158, 37, 98),
            "pressed_bg_color_secondary": (130, 30, 80),
        })
        return styles

class ButtonGradientYellow(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (255, 193, 7),
            "bg_color_secondary": (224, 168, 0),
            "hover_bg_color": (224, 168, 0),
            "hover_bg_color_secondary": (193, 145, 0),
            "pressed_bg_color": (193, 145, 0),
            "pressed_bg_color_secondary": (160, 120, 0),
            "text_color": (0, 0, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonGradientLime(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (132, 204, 22),
            "bg_color_secondary": (107, 166, 18),
            "hover_bg_color": (107, 166, 18),
            "hover_bg_color_secondary": (89, 138, 15),
            "pressed_bg_color": (89, 138, 15),
            "pressed_bg_color_secondary": (70, 110, 12),
            "text_color": (0, 0, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonGradientGreen(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (40, 167, 69),
            "bg_color_secondary": (33, 136, 56),
            "hover_bg_color": (33, 136, 56),
            "hover_bg_color_secondary": (25, 105, 44),
            "pressed_bg_color": (25, 105, 44),
            "pressed_bg_color_secondary": (20, 85, 35),
        })
        return styles

class ButtonGradientLightBlue(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (13, 202, 240),
            "bg_color_secondary": (11, 172, 204),
            "hover_bg_color": (11, 172, 204),
            "hover_bg_color_secondary": (9, 149, 176),
            "pressed_bg_color": (9, 149, 176),
            "pressed_bg_color_secondary": (7, 120, 142),
            "text_color": (0, 0, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0)
        })
        return styles

class ButtonGradientBlue(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (0, 123, 255),
            "bg_color_secondary": (0, 86, 214),
            "hover_bg_color": (0, 86, 214),
            "hover_bg_color_secondary": (0, 64, 166),
            "pressed_bg_color": (0, 64, 166),
            "pressed_bg_color_secondary": (0, 50, 130),
        })
        return styles

class ButtonGradientPurple(ButtonGradientBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (111, 66, 193),
            "bg_color_secondary": (94, 56, 164),
            "hover_bg_color": (94, 56, 164),
            "hover_bg_color_secondary": (79, 47, 138),
            "pressed_bg_color": (79, 47, 138),
            "pressed_bg_color_secondary": (65, 39, 115),
        })
        return styles


""" --------------------------- """
""" STYLE 4: NEUMORPHIC BUTTONS """
""" --------------------------- """

class ButtonNeumorphicBase(Button):
    """
    Base class for 'neumorphic' buttons.
    Soft 3D effect with shadows and highlights.
    """
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        styles.update({
            "bg_color": (225, 225, 225),
            "hover_bg_color": (235, 235, 235),
            "pressed_bg_color": (215, 215, 215),
            "text_color": (60, 60, 60),
            "hover_text_color": (40, 40, 40),
            "pressed_text_color": (80, 80, 80),
            "border_radius": 15,
            "shadow_offset": 6,
            "highlight_offset": -6,
        })
        return styles
    
    def draw(self, surface: pg.Surface):
        if not self._visible:
            return
        
        # Determinar colores
        if not self._enabled:
            bg_color = self._styles["disabled_bg_color"]
            text_color = self._styles["disabled_text_color"]
            shadow_intensity = 0.3
        elif self._pressed:
            bg_color = self._styles["pressed_bg_color"]
            text_color = self._styles["pressed_text_color"]
            shadow_intensity = 0.5
        elif self._hovered:
            bg_color = self._styles["hover_bg_color"]
            text_color = self._styles["hover_text_color"]
            shadow_intensity = 1.2
        else:
            bg_color = self._styles["bg_color"]
            text_color = self._styles["text_color"]
            shadow_intensity = 1.0
        
        offset = self._styles.get("shadow_offset", 6)
        radius = self._styles["border_radius"]
        
        # Sombra oscura (abajo-derecha)
        if not self._pressed:
            shadow_color = tuple(max(0, int(c * 0.7 * shadow_intensity)) for c in bg_color)
            shadow_rect = self._rect.copy()
            shadow_rect.x += offset
            shadow_rect.y += offset
            pg.draw.rect(surface, shadow_color, shadow_rect, border_radius=radius)
        
        # Highlight claro (arriba-izquierda)
        if not self._pressed:
            highlight_color = tuple(min(255, int(c * 1.15 * shadow_intensity)) for c in bg_color)
            highlight_rect = self._rect.copy()
            highlight_rect.x -= offset // 2
            highlight_rect.y -= offset // 2
            pg.draw.rect(surface, highlight_color, highlight_rect, border_radius=radius)
        
        # Fondo principal
        pg.draw.rect(surface, bg_color, self._rect, border_radius=radius)
        
        # Borde sutil
        border_color = tuple(max(0, int(c * 0.9)) for c in bg_color)
        pg.draw.rect(surface, border_color, self._rect, border_radius=radius, width=1)
        
        # Texto
        if self._text:
            if not hasattr(self, "_last_text_color") or self._last_text_color != text_color:
                self._text_surface = self._font.render(self._text, True, text_color)
                self._last_text_color = text_color
            
            padding_x, padding_y = self._styles["padding"]
            content_rect = self._rect.inflate(-padding_x * 2, -padding_y * 2)
            text_rect = self._text_surface.get_rect(center=content_rect.center)
            surface.blit(self._text_surface, text_rect)

class ButtonNeumorphicGray(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (200, 200, 200)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 15) for c in base),
            "pressed_bg_color": tuple(max(0, c - 15) for c in base),
            "text_color": (60, 60, 60),
        })
        return styles

class ButtonNeumorphicBlack(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (80, 80, 80)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 20) for c in base),
            "pressed_bg_color": tuple(max(0, c - 10) for c in base),
            "text_color": (220, 220, 220),
            "hover_text_color": (240, 240, 240),
            "pressed_text_color": (200, 200, 200),
        })
        return styles

class ButtonNeumorphicBrown(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (160, 120, 95)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 15) for c in base),
            "pressed_bg_color": tuple(max(0, c - 15) for c in base),
            "text_color": (50, 30, 20),
        })
        return styles

class ButtonNeumorphicOrange(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (255, 160, 100)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (80, 40, 10),
        })
        return styles

class ButtonNeumorphicRed(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (240, 120, 120)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (100, 20, 20),
        })
        return styles

class ButtonNeumorphicPink(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (240, 150, 190)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (100, 30, 60),
        })
        return styles

class ButtonNeumorphicYellow(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (255, 230, 120)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (80, 70, 10),
        })
        return styles

class ButtonNeumorphicLime(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (180, 230, 120)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (40, 80, 20),
        })
        return styles

class ButtonNeumorphicGreen(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (140, 210, 150)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (20, 80, 30),
        })
        return styles

class ButtonNeumorphicLightBlue(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (150, 220, 250)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 5) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (10, 60, 80),
        })
        return styles

class ButtonNeumorphicBlue(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (130, 180, 240)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (20, 40, 100),
        })
        return styles

class ButtonNeumorphicPurple(ButtonNeumorphicBase):
    def _get_default_styles(self) -> Dict[str, Any]:
        styles = super()._get_default_styles()
        base = (180, 140, 220)
        styles.update({
            "bg_color": base,
            "hover_bg_color": tuple(min(255, c + 10) for c in base),
            "pressed_bg_color": tuple(max(0, c - 20) for c in base),
            "text_color": (60, 30, 100),
        })
        return styles