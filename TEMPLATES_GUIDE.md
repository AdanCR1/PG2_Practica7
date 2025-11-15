# Predefined Templates Guide - pygame_ui_items v0.1.0

This guide documents all the predefined templates available in the library. **Each template can be customized simply by changing the color**, maintaining simplicity and design power.

---

## Index

- [Button Templates](#-button-templates)
- [Modal Templates](#-modal-templates)
- [Usage Examples](#-usage-examples)

---

## Button Templates

### **4 Styles × 12 Colors = 48 Variations**

#### **Style 1: Solid**
Buttons with solid color background and hover/pressed effects.

```python
# Basic example - Just change the color
button_red("My Button", my_callback, x=100, y=100)
button_blue("My Button", my_callback, x=100, y=100)
button_green("My Button", my_callback, x=100, y=100)
```

**Available colors:**
- `button_gray()` - Professional gray
- `button_black()` - Elegant black  
- `button_brown()` - Warm brown
- `button_orange()` - Vibrant orange
- `button_red()` - Action red
- `button_pink()` - Modern pink
- `button_yellow()` - Bright yellow
- `button_lime()` - Energetic lime
- `button_green()` - Success green
- `button_light_blue()` - Light blue
- `button_blue()` - Main blue
- `button_purple()` - Creative purple

![Alt text](images\buttons_solid.png)

---

#### **Style 2: Outline**
Transparent buttons with colored border. On hover, it inverts (colored background).

```python
# Basic example - Just change the color
button_outline_red("My Button", my_callback, x=100, y=100)
button_outline_blue("My Button", my_callback, x=100, y=100)
button_outline_green("My Button", my_callback, x=100, y=100)
```

**Available colors:**
- `button_outline_gray()` - Gray outline
- `button_outline_black()` - Black outline
- `button_outline_brown()` - Brown outline
- `button_outline_orange()` - Orange outline
- `button_outline_red()` - Red outline
- `button_outline_pink()` - Pink outline
- `button_outline_yellow()` - Yellow outline
- `button_outline_lime()` - Lime outline
- `button_outline_green()` - Green outline
- `button_outline_light_blue()` - Light blue outline
- `button_outline_blue()` - Blue outline
- `button_outline_purple()` - Purple outline

![Alt text](images\buttons_outline.png)

---

#### **Style 3: Gradient**
Buttons with vertical gradient effect for a modern look.

```python
# Basic example - Just change the color
button_gradient_red("My Button", my_callback, x=100, y=100)
button_gradient_blue("My Button", my_callback, x=100, y=100)
button_gradient_green("My Button", my_callback, x=100, y=100)
```

**Available colors:**
- `button_gradient_gray()` - Gray gradient
- `button_gradient_black()` - Black gradient
- `button_gradient_brown()` - Brown gradient
- `button_gradient_orange()` - Orange gradient
- `button_gradient_red()` - Red gradient
- `button_gradient_pink()` - Pink gradient
- `button_gradient_yellow()` - Yellow gradient
- `button_gradient_lime()` - Lime gradient
- `button_gradient_green()` - Green gradient
- `button_gradient_light_blue()` - Light blue gradient
- `button_gradient_blue()` - Blue gradient
- `button_gradient_purple()` - Purple gradient

![Alt text](images\buttons_gradient.png)

---

#### **Style 4: Neumorphic**
Buttons with soft 3D effect, shadows and highlights for a modern neumorphic design.

```python
# Basic example - Just change the color
button_neumorphic_red("My Button", my_callback, x=100, y=100)
button_neumorphic_blue("My Button", my_callback, x=100, y=100)
button_neumorphic_green("My Button", my_callback, x=100, y=100)
```

**Available colors:**
- `button_neumorphic_gray()` - Neumorphic gray
- `button_neumorphic_black()` - Neumorphic black
- `button_neumorphic_brown()` - Neumorphic brown
- `button_neumorphic_orange()` - Neumorphic orange
- `button_neumorphic_red()` - Neumorphic red
- `button_neumorphic_pink()` - Neumorphic pink
- `button_neumorphic_yellow()` - Neumorphic yellow
- `button_neumorphic_lime()` - Neumorphic lime
- `button_neumorphic_green()` - Neumorphic green
- `button_neumorphic_light_blue()` - Neumorphic light blue
- `button_neumorphic_blue()` - Neumorphic blue
- `button_neumorphic_purple()` - Neumorphic purple

![Alt text](images\buttons_neumorphic.png)

---

## Modal Templates

### **7 Predefined Templates**

#### **1. Alert Modal**
Basic modal with a single "OK" button.

```python
modal = create_alert_modal(
    screen_width, screen_height, 
    "This is an alert!", 
    on_close=my_callback
)
```

---

#### **2. Confirmation Modal**
Modal with two buttons: "Confirm" and "Cancel".

```python
modal = create_confirm_modal(
    screen_width, screen_height,
    "Are you sure?",
    on_confirm=confirm_callback,
    on_cancel=cancel_callback
)
```

---

#### **3. Error Modal**
Error modal with red button and red text.

```python
modal = create_error_modal(
    screen_width, screen_height,
    "An error occurred!",
    on_close=my_callback
)
```

---

#### **4. Success Modal**
Success modal with ✓ symbol, green colors and "Continue" button.

```python
modal = create_success_modal(
    screen_width, screen_height,
    "Operation completed!",
    on_close=my_callback
)
```

---

#### **5. Warning Modal**
Warning modal with ⚠ symbol, yellow colors and "Proceed"/"Cancel" buttons.

```python
modal = create_warning_modal(
    screen_width, screen_height,
    "This action cannot be undone",
    on_proceed=proceed_callback,
    on_cancel=cancel_callback
)
```

---

#### **6. Info Modal**
Informative modal with ℹ symbol, blue colors and "Understood" button.

```python
modal = create_info_modal(
    screen_width, screen_height,
    "Important system information",
    on_close=my_callback
)
```

---

#### **7. Input Modal**
Modal with text input field, "Submit"/"Cancel" buttons.

```python
def handle_text_input(user_input):
    print(f"User entered: {user_input}")

modal = create_input_modal(
    screen_width, screen_height,
    "Enter your name:",
    "Type here...",
    on_submit=handle_text_input,
    on_cancel=cancel_callback
)
```

---

## Usage Examples

### **Complete Example: Change Only the Color**

```python
import pygame as pg
from pygame_ui_items import *

pg.init()
screen = pg.display.set_mode((800, 600))
ui_manager = UIManager()

# SAME code, DIFFERENT colors - It's that simple!
btn1 = button_red("Delete", lambda: print("Deleted"), x=100, y=100)
btn2 = button_green("Save", lambda: print("Saved"), x=250, y=100)  
btn3 = button_blue("Info", lambda: print("Info"), x=400, y=100)

# Different styles, SAME usage
btn4 = button_outline_purple("Outline", lambda: print("Outline"), x=100, y=150)
btn5 = button_gradient_orange("Gradient", lambda: print("Gradient"), x=250, y=150)
btn6 = button_neumorphic_pink("Neumorphic", lambda: print("Neumorphic"), x=400, y=150)

for btn in [btn1, btn2, btn3, btn4, btn5, btn6]:
    ui_manager.add_element(btn)

# Main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False
        ui_manager.handle_event(event)
    
    ui_manager.update()
    screen.fill((240, 240, 240))
    ui_manager.draw(screen)
    pg.display.flip()

pg.quit()
```

### **Example: All Modals**

```python
# Function to close modal
def close():
    ui_manager.window_stack.pop()

# 7 different modals, SAME usage pattern
modals = [
    create_alert_modal(800, 600, "Alert", close),
    create_confirm_modal(800, 600, "Confirm?", close, close),
    create_error_modal(800, 600, "Error", close),
    create_success_modal(800, 600, "Success!", close),
    create_warning_modal(800, 600, "Warning", close, close),
    create_info_modal(800, 600, "Info", close),
    create_input_modal(800, 600, "Name:", "Type...", lambda t: print(t), close)
]

# Open any modal
ui_manager.window_stack.push(modals[0])  # Alert
```

---

## Design Philosophy

### **Extreme Simplicity**
```python
# ❌ Before (complex)
button = Button(100, 100, 120, 40, "Text", callback)
button.set_bg_color((255, 0, 0))
button.set_hover_color((200, 0, 0))
button.set_pressed_color((150, 0, 0))

# ✅ Now (simple)
button = button_red("Text", callback, x=100, y=100)
```

### **Powerful Customization**
```python
# Customize any aspect while keeping the template
button = button_blue(
    "My Button", 
    callback, 
    x=100, y=100,
    width=200,           # Custom size
    height=60,
    border_radius=20,    # More rounded
    font_size=24         # Larger text
)
```

### **Visual Consistency**
- **12 carefully selected colors**
- **4 styles** that work with all colors  
- **7 modals** with iconography and semantic colors
- **Same API** for all variations

---

## Run the Showcase

To see all templates in action:

```bash
python example_complete_showcase.py
```

**Controls:**
- **Click** buttons to test styles
- **Keys 1-7** to open different modals
- **ESC** to close current modal
- **Q** to exit

---

*This guide documents pygame_ui_items v0.1.0 - A library that makes UI creation in Pygame as simple as changing a color.*
