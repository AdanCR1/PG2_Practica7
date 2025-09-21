import pygame as pg
from typing import Callable, Dict, Any
from .helpers import lerp

class Animation:
    """Sistema de animaciones para elementos UI"""
    
    def __init__(self, duration: float = 0.3):
        self.duration = duration
        self.current_time = 0
        self.animating = False
        self.callback = None
        self.start_values = {}
        self.end_values = {}
    
    def start(self, start_values: Dict[str, Any], end_values: Dict[str, Any], 
             callback: Callable = None):
        """Inicia una animación"""
        self.start_values = start_values
        self.end_values = end_values
        self.current_time = 0
        self.animating = True
        self.callback = callback
    
    def update(self, dt: float) -> Dict[str, Any]:
        """Actualiza la animación y devuelve valores interpolados"""
        if not self.animating:
            return self.end_values
        
        self.current_time += dt
        progress = min(self.current_time / self.duration, 1.0)
        
        result = {}
        for key in self.start_values:
            if key in self.end_values:
                start_val = self.start_values[key]
                end_val = self.end_values[key]
                result[key] = lerp(start_val, end_val, progress)
        
        if progress >= 1.0:
            self.animating = False
            if self.callback:
                self.callback()
        
        return result
    
    def stop(self):
        """Detiene la animación"""
        self.animating = False

class ColorAnimation(Animation):
    """Animación específica para cambios de color"""
    
    def __init__(self, duration: float = 0.2):
        super().__init__(duration)
    
    def animate_color(self, start_color, end_color, callback=None):
        """Animación entre dos colores"""
        self.start({
            'r': start_color[0], 'g': start_color[1], 'b': start_color[2]
        }, {
            'r': end_color[0], 'g': end_color[1], 'b': end_color[2]
        }, callback)
    
    def get_current_color(self) -> tuple:
        """Obtiene el color actual de la animación"""
        if not self.animating:
            if self.end_values:
                return (self.end_values['r'], self.end_values['g'], self.end_values['b'])
            return (0, 0, 0)
        
        values = self.update(pg.time.get_ticks() / 1000)
        return (int(values['r']), int(values['g']), int(values['b']))