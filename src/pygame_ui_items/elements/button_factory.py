from typing import Callable
from button import Button, RedButton, BlueButton, GreenButton, YellowButton

# FUNCIONES FACTORY CORREGIDAS (sin duplicación de parámetros)
def button_red(text: str, onclick: Callable = None, **kwargs) -> RedButton:
    x = kwargs.pop('x', 0)
    y = kwargs.pop('y', 0)
    width = kwargs.pop('width', 120)
    height = kwargs.pop('height', 40)
    btn = RedButton(x, y, width, height, text, onclick, **kwargs)
    return btn

def button_blue(text: str, onclick: Callable = None, **kwargs) -> BlueButton:
    x = kwargs.pop('x', 0)
    y = kwargs.pop('y', 0)
    width = kwargs.pop('width', 120)
    height = kwargs.pop('height', 40)
    btn = BlueButton(x, y, width, height, text, onclick, **kwargs)
    return btn

def button_green(text: str, onclick: Callable = None, **kwargs) -> GreenButton:
    x = kwargs.pop('x', 0)
    y = kwargs.pop('y', 0)
    width = kwargs.pop('width', 120)
    height = kwargs.pop('height', 40)
    btn = GreenButton(x, y, width, height, text, onclick, **kwargs)
    return btn

def button_yellow(text: str, onclick: Callable = None, **kwargs) -> YellowButton:
    x = kwargs.pop('x', 0)
    y = kwargs.pop('y', 0)
    width = kwargs.pop('width', 120)
    height = kwargs.pop('height', 40)
    btn = YellowButton(x, y, width, height, text, onclick, **kwargs)
    return btn

def create_button(text: str, onclick: Callable = None, **kwargs) -> Button:
    x = kwargs.pop('x', 0)
    y = kwargs.pop('y', 0)
    width = kwargs.pop('width', 120)
    height = kwargs.pop('height', 40)
    btn = Button(x, y, width, height, text, onclick, **kwargs)
    return btn