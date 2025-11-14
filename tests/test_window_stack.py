import pytest
from pygame_ui_items.window_stack import Window, WindowStack

class MockEvent:
    def __init__(self, type):
        self.type = type

class MockWindow(Window):
    def __init__(self):
        super().__init__(0, 0, 100, 100)
        self.event_handled = False
        self.updated = False
        self.drawn = False

    def handle_event(self, event: MockEvent) -> bool:
        self.event_handled = True
        return True
    
    def update(self):
        self.updated = True
    
    def draw(self, surface):
        self.drawn = True

@pytest.fixture
def stack():
    return WindowStack()

@pytest.fixture
def window1():
    return MockWindow()

@pytest.fixture
def window2():
    return MockWindow()

def test_stack_init(stack):
    assert stack.is_empty()
    assert stack.peek() is None

def test_stack_push(stack, window1):
    stack.push(window1)
    assert not stack.is_empty()
    assert stack.peek() == window1

def test_stack_push_multiple(stack, window1, window2):
    stack.push(window1)
    stack.push(window2)
    assert not stack.is_empty()
    assert stack.peek() == window2

def test_stack_pop(stack, window1, window2):
    stack.push(window1)
    stack.push(window2)
    
    popped = stack.pop()
    assert popped == window2
    assert stack.peek() == window1
    
    popped = stack.pop()
    assert popped == window1
    assert stack.is_empty()

def test_stack_pop_empty(stack):
    popped = stack.pop()
    assert popped is None
    assert stack.is_empty()

def test_stack_handle_event_only_top(stack, window1, window2):
    """Prueba clave: solo la ventana de arriba debe recibir eventos"""
    stack.push(window1)
    stack.push(window2)
    
    mock_event = MockEvent(type=1)
    stack.handle_event(mock_event)
    
    assert window2.event_handled == True
    assert window1.event_handled == False

def test_stack_update_only_top(stack, window1, window2):
    stack.push(window1)
    stack.push(window2)
    
    stack.update()
    
    assert window2.updated == True
    assert window1.updated == False

def test_stack_draw_only_top(stack, window1, window2):
    stack.push(window1)
    stack.push(window2)
    
    stack.draw(surface=None)
    
    assert window2.drawn == True
    assert window1.drawn == False

def test_stack_handle_event_empty(stack):
    mock_event = MockEvent(type=1)
    handled = stack.handle_event(mock_event)
    assert handled == False