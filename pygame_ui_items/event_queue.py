import pygame as pg
from typing import Callable, Optional, Any
from dataclasses import dataclass, field
import heapq

@dataclass(order=True)
class UIEvent:
    """Representa un evento en la cola de prioridad"""
    priority: int
    timestamp: float = field(compare=False)
    event_type: str = field(compare=False)
    callback: Callable = field(compare=False)
    data: Any = field(default=None, compare=False)
    delay: float = field(default=0.0, compare=False)
    _executed: bool = field(default=False, compare=False, init=False)
    
    def execute(self):
        """Ejecuta el callback del evento"""
        if not self._executed and self.callback:
            self._executed = True
            if self.data is not None:
                self.callback(self.data)
            else:
                self.callback()
            return True
        return False
    
    def is_ready(self, current_time: float) -> bool:
        """Verifica si el evento está listo para ejecutarse"""
        return not self._executed and (current_time - self.timestamp >= self.delay)


class EventQueue:
    """
    Cola de prioridad para manejar eventos UI con delays y prioridades.
    
    Prioridades (menor número = mayor prioridad):
    0 = CRITICAL (eventos críticos del sistema)
    1 = HIGH (eventos importantes)
    2 = NORMAL (eventos normales)
    3 = LOW (eventos de baja prioridad)
    """
    
    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3
    
    def __init__(self):
        self._queue = []
        self._event_count = 0
        self._start_time = pg.time.get_ticks() / 1000.0
    
    def add_event(self, 
                  callback: Callable, 
                  priority: int = NORMAL,
                  event_type: str = "generic",
                  delay: float = 0.0,
                  data: Any = None):
        """
        Agrega un evento a la cola de prioridad.
        
        Args:
            callback: Función a ejecutar
            priority: Prioridad del evento (0-3)
            event_type: Tipo de evento (para identificación)
            delay: Delay en segundos antes de ejecutar
            data: Datos opcionales para pasar al callback
        """
        current_time = self._get_current_time()
        event = UIEvent(
            priority=priority,
            timestamp=current_time,
            event_type=event_type,
            callback=callback,
            data=data,
            delay=delay
        )
        heapq.heappush(self._queue, event)
        self._event_count += 1
    
    def process_events(self):
        """Procesa todos los eventos que están listos para ejecutarse"""
        current_time = self._get_current_time()
        executed = []
        
        while self._queue:
            event = heapq.heappop(self._queue)
            
            if event.is_ready(current_time):
                if event.execute():
                    executed.append(event)
            else:
                # Si no está listo, lo devolvemos a la cola
                heapq.heappush(self._queue, event)
                break
        
        return executed
    
    def peek(self) -> Optional[UIEvent]:
        """Obtiene el siguiente evento sin removerlo de la cola"""
        return self._queue[0] if self._queue else None
    
    def clear(self):
        """Limpia toda la cola de eventos"""
        self._queue.clear()
    
    def size(self) -> int:
        """Retorna el número de eventos pendientes"""
        return len(self._queue)
    
    def is_empty(self) -> bool:
        """Verifica si la cola está vacía"""
        return len(self._queue) == 0
    
    def get_events_by_type(self, event_type: str) -> list:
        """Obtiene todos los eventos de un tipo específico"""
        return [e for e in self._queue if e.event_type == event_type]
    
    def remove_events_by_type(self, event_type: str):
        """Remueve todos los eventos de un tipo específico"""
        self._queue = [e for e in self._queue if e.event_type != event_type]
        heapq.heapify(self._queue)
    
    def _get_current_time(self) -> float:
        """Obtiene el tiempo actual en segundos"""
        return pg.time.get_ticks() / 1000.0
    
    def get_stats(self) -> dict:
        """Obtiene estadísticas de la cola"""
        return {
            "pending_events": len(self._queue),
            "total_processed": self._event_count - len(self._queue),
            "total_events": self._event_count
        }