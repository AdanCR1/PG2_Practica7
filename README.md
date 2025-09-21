# pygame_ui_items

pygame_ui_items es una librería open-source para Python que proporciona herramientas para la creación y gestión de elementos de interfaz de usuario (UI) en Pygame, con un enfoque en la personalización, uso de una sintaxis tipo CSS para los estilos y facilidad de uso. Actualmente en la versión 0.1.0, se centra en la creación de botones, permitiendo definirlos en una sola línea de código y modificarlos con total libertad.
Por el momento, la librería incluye:
- Botones (Button): Permite crear botones con texto, posición, tamaño y estilo definido de manera similar a CSS.
- Temas (Themes): Permite cambiar la apariencia de los botones de manera sencilla (posteriormente se añadirán más elementos UI a los que se les podrá aplicar estilos).

## Tabla de Contenidos

- [Instalación](#instalación)
- [Características](#características)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Pautas de Contribución](#pautas-de-contribución)
- [Licencia](#licencia)

## Instalación

Puedes instalar pygame_ui_items usando pip:

```bash
pip install pygame_ui_items
```

Asegúrate también de tener Pygame instalado. Puedes instalarlo usando:

```bash
pip install pygame
```

---

## Características

- Creación de Botones en una Línea: Define botones con texto, posición, tamaño y estilo similar a CSS.
- Personalización Completa: Modifica los botones por defecto o crea nuevos con estilos personalizados.
- Fácil Integración: Se integra perfectamente con el ciclo principal de Pygame.
- Temas: Permite cambiar la apariencia de los botones de manera sencilla.

---

## Ejemplos de Uso

### 1. Creación de un botón simple

```python
import pygame
from pygame_ui_items.core.ui_manager import UIManager
from pygame_ui_items.elements.button import Button

pygame.init()
screen = pygame.display.set_mode((800, 600))
ui_manager = UIManager(screen)

button = Button("Click Me", (100, 100), ui_manager) # Boton creado en una sola línea en lugar de 6 o mas

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ui_manager.process_events(event)

    ui_manager.update()
    screen.fill((255, 255, 255))
    ui_manager.draw()
    pygame.display.flip()

pygame.quit()
```

### 2. Modificación de Estilos

```python
import pygame
from pygame_ui_items.core.ui_manager import UIManager
from pygame_ui_items.elements.button import Button
from pygame_ui_items.styles.themes import Theme

pygame.init()
screen = pygame.display.set_mode((800, 600))
ui_manager = UIManager(screen)

# Crear un tema personalizado
custom_theme = Theme({
    "normal_bg": (200, 200, 200),
    "hover_bg": (220, 220, 220),
    "text_color": (0, 0, 0),
    "font_size": 24
})

button = Button("Click Me", (100, 100), ui_manager, theme=custom_theme)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ui_manager.process_events(event)

    ui_manager.update()
    screen.fill((255, 255, 255))
    ui_manager.draw()
    pygame.display.flip()

pygame.quit()
```

### 3. Ejemplo completo (imagen)

![Ejemplo Completo](../PG2_Practica7/images/example-complete_image.png)

## Pautas de Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'feat: Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.