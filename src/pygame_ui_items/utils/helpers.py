import pygame as pg
from typing import Tuple

def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convierte color HEX a RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """Convierte RGB a HEX"""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def lerp(start: float, end: float, factor: float) -> float:
    """Interpolación lineal"""
    return start + (end - start) * factor

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Limita un valor entre mínimo y máximo"""
    return max(min_val, min(value, max_val))

def is_point_in_rect(point: Tuple[int, int], rect: pg.Rect) -> bool:
    """Verifica si un punto está dentro de un rectángulo"""
    return rect.collidepoint(point)

def calculate_text_size(text: str, font: pg.font.Font) -> Tuple[int, int]:
    """Calcula el tamaño del texto renderizado"""
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface.get_size()

def create_gradient_surface(width: int, height: int, 
                          start_color: Tuple[int, int, int], 
                          end_color: Tuple[int, int, int],
                          vertical: bool = True) -> pg.Surface:
    """Crea una superficie con gradiente de color"""
    surface = pg.Surface((width, height), pg.SRCALPHA)
    
    if vertical:
        for y in range(height):
            ratio = y / height
            r = lerp(start_color[0], end_color[0], ratio)
            g = lerp(start_color[1], end_color[1], ratio)
            b = lerp(start_color[2], end_color[2], ratio)
            pg.draw.line(surface, (r, g, b), (0, y), (width, y))
    else:
        for x in range(width):
            ratio = x / width
            r = lerp(start_color[0], end_color[0], ratio)
            g = lerp(start_color[1], end_color[1], ratio)
            b = lerp(start_color[2], end_color[2], ratio)
            pg.draw.line(surface, (r, g, b), (x, 0), (x, height))
    
    return surface