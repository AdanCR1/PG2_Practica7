from typing import Callable
from pygame_ui_items.button import *

""" 
    This module implements factory functions for creating buttons.
    Each function simplifies instantiation with default parameters.
"""

def create_button(text: str, onclick: Callable = None, **kwargs) -> Button:
    x = kwargs.pop('x', 0)
    y = kwargs.pop('y', 0)
    width = kwargs.pop('width', 120)
    height = kwargs.pop('height', 40)
    btn = Button(x, y, width, height, text, onclick, **kwargs)
    return btn

"""
    STYLE 1: SOLID COLOR BUTTONS
"""

def button_gray(text: str, onclick: Callable = None, **kwargs) -> ButtonGray:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGray(x, y, w, h, text, onclick, **kwargs)

def button_black(text: str, onclick: Callable = None, **kwargs) -> ButtonBlack:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonBlack(x, y, w, h, text, onclick, **kwargs)

def button_brown(text: str, onclick: Callable = None, **kwargs) -> ButtonBrown:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonBrown(x, y, w, h, text, onclick, **kwargs)

def button_orange(text: str, onclick: Callable = None, **kwargs) -> ButtonOrange:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOrange(x, y, w, h, text, onclick, **kwargs)

def button_red(text: str, onclick: Callable = None, **kwargs) -> ButtonRed:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonRed(x, y, w, h, text, onclick, **kwargs)

def button_pink(text: str, onclick: Callable = None, **kwargs) -> ButtonPink:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonPink(x, y, w, h, text, onclick, **kwargs)

def button_yellow(text: str, onclick: Callable = None, **kwargs) -> ButtonYellow:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonYellow(x, y, w, h, text, onclick, **kwargs)

def button_lime(text: str, onclick: Callable = None, **kwargs) -> ButtonLime:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonLime(x, y, w, h, text, onclick, **kwargs)

def button_green(text: str, onclick: Callable = None, **kwargs) -> ButtonGreen:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGreen(x, y, w, h, text, onclick, **kwargs)

def button_light_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonLightBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonLightBlue(x, y, w, h, text, onclick, **kwargs)

def button_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonBlue(x, y, w, h, text, onclick, **kwargs)

def button_purple(text: str, onclick: Callable = None, **kwargs) -> ButtonPurple:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonPurple(x, y, w, h, text, onclick, **kwargs)


"""
    STYLE 2: OUTLINE BUTTONS
"""

def button_outline_gray(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineGray:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineGray(x, y, w, h, text, onclick, **kwargs)

def button_outline_black(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineBlack:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineBlack(x, y, w, h, text, onclick, **kwargs)

def button_outline_brown(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineBrown:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineBrown(x, y, w, h, text, onclick, **kwargs)

def button_outline_orange(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineOrange:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineOrange(x, y, w, h, text, onclick, **kwargs)

def button_outline_red(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineRed:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineRed(x, y, w, h, text, onclick, **kwargs)

def button_outline_pink(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlinePink:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlinePink(x, y, w, h, text, onclick, **kwargs)

def button_outline_yellow(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineYellow:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineYellow(x, y, w, h, text, onclick, **kwargs)

def button_outline_lime(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineLime:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineLime(x, y, w, h, text, onclick, **kwargs)

def button_outline_green(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineGreen:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineGreen(x, y, w, h, text, onclick, **kwargs)

def button_outline_light_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineLightBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineLightBlue(x, y, w, h, text, onclick, **kwargs)

def button_outline_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlineBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlineBlue(x, y, w, h, text, onclick, **kwargs)

def button_outline_purple(text: str, onclick: Callable = None, **kwargs) -> ButtonOutlinePurple:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonOutlinePurple(x, y, w, h, text, onclick, **kwargs)


"""
    STYLE 3: GRADIENT BUTTONS
"""

def button_gradient_gray(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientGray:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientGray(x, y, w, h, text, onclick, **kwargs)

def button_gradient_black(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientBlack:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientBlack(x, y, w, h, text, onclick, **kwargs)

def button_gradient_brown(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientBrown:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientBrown(x, y, w, h, text, onclick, **kwargs)

def button_gradient_orange(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientOrange:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientOrange(x, y, w, h, text, onclick, **kwargs)

def button_gradient_red(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientRed:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientRed(x, y, w, h, text, onclick, **kwargs)

def button_gradient_pink(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientPink:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientPink(x, y, w, h, text, onclick, **kwargs)

def button_gradient_yellow(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientYellow:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientYellow(x, y, w, h, text, onclick, **kwargs)

def button_gradient_lime(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientLime:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientLime(x, y, w, h, text, onclick, **kwargs)

def button_gradient_green(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientGreen:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientGreen(x, y, w, h, text, onclick, **kwargs)

def button_gradient_light_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientLightBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientLightBlue(x, y, w, h, text, onclick, **kwargs)

def button_gradient_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientBlue(x, y, w, h, text, onclick, **kwargs)

def button_gradient_purple(text: str, onclick: Callable = None, **kwargs) -> ButtonGradientPurple:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonGradientPurple(x, y, w, h, text, onclick, **kwargs)


"""
    STYLE 4: NEUMORPHIC BUTTONS
"""

def button_neumorphic_gray(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicGray:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicGray(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_black(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicBlack:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicBlack(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_brown(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicBrown:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicBrown(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_orange(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicOrange:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicOrange(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_red(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicRed:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicRed(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_pink(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicPink:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicPink(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_yellow(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicYellow:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicYellow(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_lime(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicLime:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicLime(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_green(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicGreen:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicGreen(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_light_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicLightBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicLightBlue(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_blue(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicBlue:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicBlue(x, y, w, h, text, onclick, **kwargs)

def button_neumorphic_purple(text: str, onclick: Callable = None, **kwargs) -> ButtonNeumorphicPurple:
    x, y = kwargs.pop('x', 0), kwargs.pop('y', 0)
    w, h = kwargs.pop('width', 120), kwargs.pop('height', 40)
    return ButtonNeumorphicPurple(x, y, w, h, text, onclick, **kwargs)