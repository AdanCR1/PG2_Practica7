import pytest
import pygame as pg
import time
from pygame_ui_items.event_queue import EventQueue, UIEvent

@pytest.fixture(autouse=True)
def pygame_setup():
    pg.init()
    yield
    pg.quit()

def test_event_queue_initialization():
    """Verifica que la cola se inicializa correctamente"""
    queue = EventQueue()
    assert queue.is_empty()
    assert queue.size() == 0

def test_add_event_to_queue():
    """Verifica que se pueden agregar eventos a la cola"""
    queue = EventQueue()
    executed = {"value": False}
    
    def callback():
        executed["value"] = True
    
    queue.add_event(callback, priority=EventQueue.NORMAL)
    assert queue.size() == 1
    assert not queue.is_empty()

def test_event_execution():
    """Verifica que los eventos se ejecutan correctamente"""
    queue = EventQueue()
    results = []
    
    def callback(data):
        results.append(data)
    
    queue.add_event(callback, data="test1", priority=EventQueue.NORMAL)
    queue.add_event(callback, data="test2", priority=EventQueue.HIGH)
    
    executed = queue.process_events()
    
    # El evento HIGH debe ejecutarse primero
    assert len(results) == 2
    assert results[0] == "test2"
    assert results[1] == "test1"

def test_event_priority_order():
    """Verifica que los eventos se ejecutan en orden de prioridad"""
    queue = EventQueue()
    results = []
    
    def callback(data):
        results.append(data)
    
    queue.add_event(callback, data="low", priority=EventQueue.LOW)
    queue.add_event(callback, data="critical", priority=EventQueue.CRITICAL)
    queue.add_event(callback, data="normal", priority=EventQueue.NORMAL)
    queue.add_event(callback, data="high", priority=EventQueue.HIGH)
    
    queue.process_events()
    
    assert results == ["critical", "high", "normal", "low"]

def test_event_with_delay():
    """Verifica que los eventos con delay no se ejecutan inmediatamente"""
    queue = EventQueue()
    executed = {"value": False}
    
    def callback():
        executed["value"] = True
    
    # Agregar evento con delay de 0.1 segundos
    queue.add_event(callback, delay=0.1)
    
    # Intentar ejecutar inmediatamente
    queue.process_events()
    assert not executed["value"]
    
    # Esperar y ejecutar nuevamente
    time.sleep(0.15)
    queue.process_events()
    assert executed["value"]

def test_peek_event():
    """Verifica que peek retorna el evento sin removerlo"""
    queue = EventQueue()
    
    def callback():
        pass
    
    queue.add_event(callback, priority=EventQueue.HIGH)
    
    event = queue.peek()
    assert event is not None
    assert queue.size() == 1

def test_clear_queue():
    """Verifica que clear remueve todos los eventos"""
    queue = EventQueue()
    
    def callback():
        pass
    
    queue.add_event(callback)
    queue.add_event(callback)
    queue.add_event(callback)
    
    assert queue.size() == 3
    
    queue.clear()
    assert queue.is_empty()
    assert queue.size() == 0

def test_get_events_by_type():
    """Verifica que se pueden filtrar eventos por tipo"""
    queue = EventQueue()
    
    def callback():
        pass
    
    queue.add_event(callback, event_type="click")
    queue.add_event(callback, event_type="hover")
    queue.add_event(callback, event_type="click")
    
    click_events = queue.get_events_by_type("click")
    assert len(click_events) == 2

def test_remove_events_by_type():
    """Verifica que se pueden remover eventos por tipo"""
    queue = EventQueue()
    
    def callback():
        pass
    
    queue.add_event(callback, event_type="click")
    queue.add_event(callback, event_type="hover")
    queue.add_event(callback, event_type="click")
    
    assert queue.size() == 3
    
    queue.remove_events_by_type("click")
    assert queue.size() == 1

def test_event_stats():
    """Verifica que las estadísticas se calculan correctamente"""
    queue = EventQueue()
    
    def callback():
        pass
    
    queue.add_event(callback)
    queue.add_event(callback)
    queue.add_event(callback)
    
    stats = queue.get_stats()
    assert stats["total_events"] == 3
    assert stats["pending_events"] == 3
    
    queue.process_events()
    
    stats = queue.get_stats()
    assert stats["total_processed"] == 3
    assert stats["pending_events"] == 0

def test_event_execution_only_once():
    """Verifica que un evento solo se ejecuta una vez"""
    queue = EventQueue()
    count = {"value": 0}
    
    def callback():
        count["value"] += 1
    
    queue.add_event(callback)
    
    queue.process_events()
    queue.process_events()
    queue.process_events()
    
    assert count["value"] == 1