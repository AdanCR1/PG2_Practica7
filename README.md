<div align="center">

# pygame_ui_items
**A modular UI library for Pygame with state management and customizable styles.**

</div>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-brightgreen.svg">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <a href="https://pypi.org/project/pygame_ui_items/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/pygame_ui_items.svg">
  </a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.7+-blue.svg">
  <img alt="Pygame" src="https://img.shields.io/badge/pygame-2.0+-green.svg">
  <img alt="Tests" src="https://img.shields.io/badge/tests-31%20passed-success.svg">
</p>

`pygame_ui_items` is an open-source library for Python that provides tools for creating and managing user interface (UI) elements in Pygame.

It focuses on **customization**, robust **state management** (Stack), and **ease of use**, allowing you to define complex components in a single line of code.

The current version (0.1.0) includes:
* **UI Manager (`UIManager`)**: Handles the event loop, updates, and drawing.
* **Buttons (`Button`)**: Customizable components with a palette of 12 colors and **4 predefined styles** (Solid, Outline, **Gradient ✨**, **Neumorphic ✨**).
* **Stack Manager (`WindowStack`)**: Controls "scenes" or windows, ensuring that only the top window receives events (ideal for menus, pause screens, etc.).
* **Modals (`Modal`)**: **7 predefined templates** for pop-up windows (`Alert`, `Confirmation`, `Error`, **Success ✨**, **Warning ✨**, **Info ✨**, **Input ✨**).
* **Event Queue (`EventQueue`) ✨**: A priority system with a heap for deferred events, notifications, and animations.

---

## Translation
* **[Spanish Version (README.es.md)](README.es.md)**

## Component Gallery
Check out all the predefined button styles with their demos!

* **[View the Component Gallery (COMPONENT_GALLERY.md)](COMPONENT_GALLERY.md)**

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage Examples](#usage-examples)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Installation

To install `pygame_ui_items`, run:

```bash
pip install pygame_ui_items
```


Make sure you also have Pygame installed. Alternatively, you can run the `requirements.txt` file, which includes Pygame and pytest:

```bash
pip install -r requirements.txt
```

## Features

- **State Management (Stack):** Use a `WindowStack` to manage game states (menus, pause, gameplay) cleanly (LIFO).

- **Hierarchical Structure (Tree):** Each `Window` or `Modal` acts as a node containing a list of child elements (buttons, text).

- **Component Factory:** Create ready-to-use buttons with a single function (`button_red()`, `button_outline_blue()`, etc.).

- **Palette of 12 Colors:** A set of 12 predefined colors (Gray, Black, Red, Blue, etc.) available for all styles.

- **Multiple Styles:** Start with two button styles (Solid and Outline) to fit your design.

- **Highly Customizable:** Pass parameters (`bg_color`, `border_radius`) to override any predefined style.

## Usage Examples

<details> <summary><b>1. Create a Simple Button</b> (Click to expand)</summary>

```python
import pygame
from pygame_ui_items.ui_manager import UIManager
from pygame_ui_items.button_factory import create_button

pygame.init()
screen = pygame.display.set_mode((800, 600))
ui_manager = UIManager()

# Create a button with a lambda function as a callback
button = create_button("Click Me", lambda: print("Clicked!"), x=100, y=100)
ui_manager.add_element(button)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ui_manager.handle_event(event) # Pass events to the manager

    ui_manager.update() # Update the manager
    screen.fill((255, 255, 255))
    ui_manager.draw(screen) # Draw the manager
    pygame.display.flip()

pygame.quit()
```

</details>

<details> <summary><b>2. Use New Styles (Solid and Outline)</b> (Click to expand)</summary>

```python
import pygame as pg
import sys
from pygame_ui_items.button_factory import button_purple, button_outline_purple

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

# Solid Style
btn_solid = button_purple("Solid", lambda: print("Solid"), x=100, y=100)

# Outline Style
btn_outline = button_outline_purple("Outline", lambda: print("Outline"), x=100, y=160)

buttons = [btn_solid, btn_outline]

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False
        for button in buttons: button.handle_event(event)
    
    screen.fill((255, 255, 255)) # White background for outline style
    for button in buttons: button.draw(screen)
    
    pg.display.flip()
    clock.tick(60)
pg.quit()
sys.exit()
```

</details>

<details> <summary><b>3. Fully Customized Button</b> (Click to expand)</summary>

```python
# You can override any style, even predefined ones
btn_custom = create_button(
    "Custom Button", 
    lambda: print("Personalized"),
    x=100, y=340,
    width=200, height=50,
    bg_color=(139, 0, 0),
    hover_bg_color=(178, 34, 34),
    text_color=(255, 255, 255),
    border_radius=70
)
```
</details>

<details> <summary><b>4. Modal Management (Stack)</b> (Click to expand)</summary>

```python
import pygame as pg
from pygame_ui_items.ui_manager import UIManager
from pygame_ui_items.button_factory import button_green
from pygame_ui_items.modal import create_alert_modal, create_confirm_modal

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ui_manager = UIManager() # The UIManager controls the stack

# --- Callbacks ---
def open_alert():
    alert_modal = create_alert_modal(
        SCREEN_WIDTH, SCREEN_HEIGHT, "This is an alert!",
        on_close=lambda: ui_manager.window_stack.pop() # Close the modal (POP)
    )
    ui_manager.window_stack.push(alert_modal) # Add the modal to the stack (PUSH)

def open_confirm():
    confirm_modal = create_confirm_modal(
        SCREEN_WIDTH, SCREEN_HEIGHT, "Are you sure?",
        on_confirm=lambda: (print("Confirmed"), ui_manager.window_stack.pop()),
        on_cancel=lambda: (print("Cancelled"), ui_manager.window_stack.pop())
    )
    ui_manager.window_stack.push(confirm_modal)

# Background buttons (only work if the stack is empty)
ui_manager.add_element(button_green("Open Alert", open_alert, x=100, y=100))
ui_manager.add_element(button_green("Open Confirmation", open_confirm, x=100, y=160))

# ... (Pygame main loop) ...
# In the loop:
# ui_manager.handle_event(event)
# ui_manager.update()
# ui_manager.draw(screen)
# ...
```
</details>

## Contribution Guidelines

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch (`git checkout -b feature/new-feature`)

3. Make your changes and commit them (`git commit -m 'feat: Add new feature'`)

4. Push to the branch (`git push origin feature/new-feature`)

5. Open a Pull Request.

> [!Note]
> Make sure to follow coding conventions and add tests for any new functionality.
> If the demo files in `/examples/` don't work, move them to the project's root folder so they can find the library.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.