<div align="center">

# pygame_ui_items
**Una librería de UI modular para Pygame con gestión de estado y estilos personalizables.**

</div>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-brightgreen.svg">
  <img alt="Licencia" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <a href="https://pypi.org/project/pygame_ui_items/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/pygame_ui_items.svg">
  </a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.7+-blue.svg">
  <img alt="Pygame" src="https://img.shields.io/badge/pygame-2.0+-green.svg">
  <img alt="Tests" src="https://img.shields.io/badge/tests-31%20passed-success.svg">
</p>

`pygame_ui_items` es una librería open-source para Python que proporciona herramientas para la creación y gestión de elementos de interfaz de usuario (UI) en Pygame.

Se enfoca en la **personalización**, una **gestión de estado** robusta (Pila/Stack) y la **facilidad de uso**, permitiendo definir componentes complejos en una sola línea de código.

La versión actual (0.1.0) incluye:
* **Gestor de UI (`UIManager`)**: Maneja el ciclo de eventos, actualización y dibujado.
* **Botones (`Button`)**: Componentes personalizables con una paleta de 12 colores y **4 estilos predefinidos** (Sólido, Contorno, **Gradiente ✨**, **Neumórfico ✨**).
* **Gestor de Pila (`WindowStack`)**: Controla "escenas" o ventanas, asegurando que solo la ventana superior reciba eventos (ideal para menús, pausa, etc.).
* **Modales (`Modal`)**: **7 plantillas** de ventanas emergentes predefinidas (`Alerta`, `Confirmación`, `Error`, **Éxito ✨**, **Advertencia ✨**, **Información ✨**, **Input ✨**).
* **Cola de Eventos (`EventQueue`) ✨**: Sistema de prioridad con heap para eventos diferidos, notificaciones y animaciones.

---

## Translation (Traducción)
* **[English Version (README.es.md)](README.es.md)**

## Galería de Componentes
¡Revisa todos los estilos de botones predefinidos con sus demos!

* **[Ver la Galería de Componentes (COMPONENT_GALLERY.md)](COMPONENT_GALLERY.md)**

## Tabla de Contenidos

- [Instalación](#instalación)
- [Características](#características)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Pautas de Contribución](#pautas-de-contribución)
- [Licencia](#licencia)

## Instalación

Para instalar `pygame_ui_items` ejecuta:

```bash
pip install pygame_ui_items
```


Asegúrate también de tener Pygame instalado. O tambien puedes ejecutar el requirements.txt que incluye Pygame y pytest:

```bash
pip install -r requirements.txt
```

## Características

- **Gestión de Estado (Pila):** Usa un WindowStack para gestionar estados de juego (menús, pausa, juego) de forma limpia (LIFO).

- **Estructura Jerárquica (Árbol):** Cada Window o Modal actúa como un nodo que contiene una lista de elementos hijos (botones, texto).

- **Fábrica de Componentes:** Crea botones listos para usar con una sola función (button_red(), button_outline_blue(), etc.).

- **Paleta de 12 Colores:** Un conjunto de 12 colores predefinidos (Gris, Negro, Rojo, Azul, etc.) disponibles para todos los estilos.

- **Múltiples Estilos:** Inicia con dos estilos de botones (Sólido y Contorno) para adaptarse a tu diseño.

- **Altamente Personalizable:** Pasa parámetros (bg_color, border_radius) para sobreescribir cualquier estilo predefinido.

## Ejemplos de Uso

<details> <summary><b>1. Crear un botón simple</b> (Click para expandir)</summary>

```python
import pygame
from pygame_ui_items.ui_manager import UIManager
from pygame_ui_items.button_factory import create_button

pygame.init()
screen = pygame.display.set_mode((800, 600))
ui_manager = UIManager()

# Create a button with a lambda function as a callback
button = create_button("Click Me", lambda: print("¡Clic!"), x=100, y=100)
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

<details> <summary><b>2. Usar los nuevos estilos (Sólido y Contorno)</b> (Click para expandir)</summary>

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

<details> <summary><b>3. Botón 100% Personalizado</b> (Click para expandir)</summary>

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

<details> <summary><b>4. Gestión de Modales (Pila)</b> (Click para expandir)</summary>

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
        SCREEN_WIDTH, SCREEN_HEIGHT, "¡Esto es una alerta!",
        on_close=lambda: ui_manager.window_stack.pop() # Close the modal (POP)
    )
    ui_manager.window_stack.push(alert_modal) # Add the modal to the stack (PUSH)

def open_confirm():
    confirm_modal = create_confirm_modal(
        SCREEN_WIDTH, SCREEN_HEIGHT, "¿Estás seguro?",
        on_confirm=lambda: (print("Confirmado"), ui_manager.window_stack.pop()),
        on_cancel=lambda: (print("Cancelado"), ui_manager.window_stack.pop())
    )
    ui_manager.window_stack.push(confirm_modal)

# Background buttons (only work if the stack is empty)
ui_manager.add_element(button_green("Abrir Alerta", open_alert, x=100, y=100))
ui_manager.add_element(button_green("Abrir Confirmación", open_confirm, x=100, y=160))

# ... (Pygame main loop) ...
# In the loop:
# ui_manager.handle_event(event)
# ui_manager.update()
# ui_manager.draw(screen)
# ...
```
</details>

## Pautas de Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.

2. Crea una nueva rama (git checkout -b feature/nueva-caracteristica).

3. Realiza tus cambios y haz commit (git commit -m 'feat: Añadir nueva característica').

4. Haz push a la rama (git push origin feature/nueva-caracteristica).

5. Abre un Pull Request.

> [!Note]
> Asegúrate de seguir las convenciones de codificación y de agregar pruebas para cualquier nueva funcionalidad.
> Si los archivos demo de /examples/ no funcionan, muévelos a la carpeta raíz del proyecto para que puedan encontrar la librería.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.