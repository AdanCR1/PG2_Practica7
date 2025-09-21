from typing import Dict, Any

class Theme:
    """Clase base para temas de la UI"""
    
    def __init__(self):
        self.styles = self._get_default_styles()
    
    def _get_default_styles(self) -> Dict[str, Any]:
        return {
            "font_name": None,
            "font_size": 16,
            "padding": (10, 5),
            "border_radius": 6,
            "border_width": 1,
            "animation_duration": 150,
        }
    
    def get_button_styles(self) -> Dict[str, Any]:
        """Estilos específicos para botones"""
        return {
            "bg_color": (100, 100, 100),
            "hover_bg_color": (120, 120, 120),
            "pressed_bg_color": (80, 80, 80),
            "disabled_bg_color": (150, 150, 150),
            "text_color": (255, 255, 255),
            "hover_text_color": (255, 255, 255),
            "pressed_text_color": (255, 255, 255),
            "disabled_text_color": (100, 100, 100),
            "border_color": (50, 50, 50),
            "hover_border_color": (70, 70, 70),
            "pressed_border_color": (30, 30, 30),
        }
    
    def apply_to_element(self, element, element_type: str = "button"):
        """Aplica los estilos del tema a un elemento"""
        if element_type == "button":
            styles = self.get_button_styles()
            for key, value in styles.items():
                if hasattr(element, f"_set_{key}"):
                    getattr(element, f"_set_{key}")(value)
                elif hasattr(element, "_styles"):
                    element._styles[key] = value

class DarkTheme(Theme):
    """Tema oscuro moderno"""
    
    def get_button_styles(self) -> Dict[str, Any]:
        base_styles = super().get_button_styles()
        base_styles.update({
            "bg_color": (50, 50, 50),
            "hover_bg_color": (70, 70, 70),
            "pressed_bg_color": (30, 30, 30),
            "border_color": (80, 80, 80),
            "border_radius": 8,
        })
        return base_styles

class LightTheme(Theme):
    """Tema claro moderno"""
    
    def get_button_styles(self) -> Dict[str, Any]:
        base_styles = super().get_button_styles()
        base_styles.update({
            "bg_color": (240, 240, 240),
            "hover_bg_color": (220, 220, 220),
            "pressed_bg_color": (200, 200, 200),
            "text_color": (0, 0, 0),
            "hover_text_color": (0, 0, 0),
            "pressed_text_color": (0, 0, 0),
            "border_color": (180, 180, 180),
            "border_radius": 8,
        })
        return base_styles

class ModernTheme(Theme):
    """Tema moderno con colores vibrantes"""
    
    def get_button_styles(self) -> Dict[str, Any]:
        base_styles = super().get_button_styles()
        base_styles.update({
            "bg_color": (0, 123, 255),
            "hover_bg_color": (0, 86, 214),
            "pressed_bg_color": (0, 64, 166),
            "border_radius": 10,
            "border_width": 0,
        })
        return base_styles