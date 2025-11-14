# 🎨 Guía de Plantillas Predefinidas - pygame_ui_items v0.1.0

Esta guía documenta todas las plantillas predefinidas disponibles en la librería. **Cada plantilla se puede personalizar simplemente cambiando el color**, manteniendo la simplicidad y potencia del diseño.

---

## 📋 Índice

- [🔘 Plantillas de Botones](#-plantillas-de-botones)
- [🔔 Plantillas de Modales](#-plantillas-de-modales)
- [💡 Ejemplos de Uso](#-ejemplos-de-uso)

---

## 🔘 Plantillas de Botones

### **4 Estilos × 12 Colores = 48 Variaciones**

#### **Estilo 1: Sólido**
Botones con fondo de color sólido y efectos hover/pressed.

```python
# Ejemplo básico - Solo cambia el color
button_red("Mi Botón", mi_callback, x=100, y=100)
button_blue("Mi Botón", mi_callback, x=100, y=100)
button_green("Mi Botón", mi_callback, x=100, y=100)
```

**Colores disponibles:**
- `button_gray()` - Gris profesional
- `button_black()` - Negro elegante  
- `button_brown()` - Marrón cálido
- `button_orange()` - Naranja vibrante
- `button_red()` - Rojo de acción
- `button_pink()` - Rosa moderno
- `button_yellow()` - Amarillo brillante
- `button_lime()` - Lima energético
- `button_green()` - Verde éxito
- `button_light_blue()` - Azul claro
- `button_blue()` - Azul principal
- `button_purple()` - Púrpura creativo

<img width="2106" height="142" alt="Captura de pantalla 2025-11-14 124338" src="https://github.com/user-attachments/assets/bbd5ad1c-3d79-4c7e-90ad-67edb0a3ed53" />


---

#### **Estilo 2: Contorno**
Botones transparentes con borde coloreado. Al hacer hover se invierte (fondo coloreado).

```python
# Ejemplo básico - Solo cambia el color
button_outline_red("Mi Botón", mi_callback, x=100, y=100)
button_outline_blue("Mi Botón", mi_callback, x=100, y=100)
button_outline_green("Mi Botón", mi_callback, x=100, y=100)
```

**Colores disponibles:**
- `button_outline_gray()` - Contorno gris
- `button_outline_black()` - Contorno negro
- `button_outline_brown()` - Contorno marrón
- `button_outline_orange()` - Contorno naranja
- `button_outline_red()` - Contorno rojo
- `button_outline_pink()` - Contorno rosa
- `button_outline_yellow()` - Contorno amarillo
- `button_outline_lime()` - Contorno lima
- `button_outline_green()` - Contorno verde
- `button_outline_light_blue()` - Contorno azul claro
- `button_outline_blue()` - Contorno azul
- `button_outline_purple()` - Contorno púrpura

<img width="2098" height="121" alt="Captura de pantalla 2025-11-14 124438" src="https://github.com/user-attachments/assets/dc859a12-4b3f-4443-b974-00d57d738818" />

---

#### **Estilo 3: Gradiente**
Botones con efecto degradado vertical para un look moderno.

```python
# Ejemplo básico - Solo cambia el color
button_gradient_red("Mi Botón", mi_callback, x=100, y=100)
button_gradient_blue("Mi Botón", mi_callback, x=100, y=100)
button_gradient_green("Mi Botón", mi_callback, x=100, y=100)
```

**Colores disponibles:**
- `button_gradient_gray()` - Gradiente gris
- `button_gradient_black()` - Gradiente negro
- `button_gradient_brown()` - Gradiente marrón
- `button_gradient_orange()` - Gradiente naranja
- `button_gradient_red()` - Gradiente rojo
- `button_gradient_pink()` - Gradiente rosa
- `button_gradient_yellow()` - Gradiente amarillo
- `button_gradient_lime()` - Gradiente lima
- `button_gradient_green()` - Gradiente verde
- `button_gradient_light_blue()` - Gradiente azul claro
- `button_gradient_blue()` - Gradiente azul
- `button_gradient_purple()` - Gradiente púrpura

<img width="2105" height="132" alt="Captura de pantalla 2025-11-14 124455" src="https://github.com/user-attachments/assets/917c5838-0c5e-48ab-a540-b4cb17493817" />

---

#### **Estilo 4: Neumórfico**
Botones con efecto 3D suave, sombras y highlights para un diseño neumórfico moderno.

```python
# Ejemplo básico - Solo cambia el color
button_neumorphic_red("Mi Botón", mi_callback, x=100, y=100)
button_neumorphic_blue("Mi Botón", mi_callback, x=100, y=100)
button_neumorphic_green("Mi Botón", mi_callback, x=100, y=100)
```

**Colores disponibles:**
- `button_neumorphic_gray()` - Neumórfico gris
- `button_neumorphic_black()` - Neumórfico negro
- `button_neumorphic_brown()` - Neumórfico marrón
- `button_neumorphic_orange()` - Neumórfico naranja
- `button_neumorphic_red()` - Neumórfico rojo
- `button_neumorphic_pink()` - Neumórfico rosa
- `button_neumorphic_yellow()` - Neumórfico amarillo
- `button_neumorphic_lime()` - Neumórfico lima
- `button_neumorphic_green()` - Neumórfico verde
- `button_neumorphic_light_blue()` - Neumórfico azul claro
- `button_neumorphic_blue()` - Neumórfico azul
- `button_neumorphic_purple()` - Neumórfico púrpura

<img width="2105" height="132" alt="Captura de pantalla 2025-11-14 124510" src="https://github.com/user-attachments/assets/a604ccfe-f206-4e06-b85a-cc29a87fc8e8" />

---

## 🔔 Plantillas de Modales

### **7 Plantillas Predefinidas**

#### **1. Modal de Alerta**
Modal básico con un solo botón "OK".

```python
modal = create_alert_modal(
    screen_width, screen_height, 
    "¡Esta es una alerta!", 
    on_close=mi_callback
)
```

<img width="567" height="312" alt="Captura de pantalla 2025-11-14 125425" src="https://github.com/user-attachments/assets/15898733-3b59-4fb0-ad19-e1ca884bc21e" />

---

#### **2. Modal de Confirmación**
Modal con dos botones: "Confirmar" y "Cancelar".

```python
modal = create_confirm_modal(
    screen_width, screen_height,
    "¿Estás seguro?",
    on_confirm=confirmar_callback,
    on_cancel=cancelar_callback
)
```

<img width="655" height="346" alt="Captura de pantalla 2025-11-14 125442" src="https://github.com/user-attachments/assets/9c9b80a5-c16d-4938-ae33-5631ffa98d24" />

---

#### **3. Modal de Error**
Modal de error con botón rojo y texto rojo.

```python
modal = create_error_modal(
    screen_width, screen_height,
    "¡Ha ocurrido un error!",
    on_close=mi_callback
)
```

<img width="545" height="289" alt="Captura de pantalla 2025-11-14 125454" src="https://github.com/user-attachments/assets/e9a239a6-7b6c-49d7-ac67-5b5d65cdb31a" />

---

#### **4. Modal de Éxito**
Modal de éxito con símbolo ✓, colores verdes y botón "Continuar".

```python
modal = create_success_modal(
    screen_width, screen_height,
    "¡Operación completada!",
    on_close=mi_callback
)
```

<img width="588" height="304" alt="Captura de pantalla 2025-11-14 125507" src="https://github.com/user-attachments/assets/f792d595-764f-4b0a-9ba3-8304eeee1965" />

---

#### **5. Modal de Advertencia**
Modal de advertencia con símbolo ⚠, colores amarillos y botones "Proceder"/"Cancelar".

```python
modal = create_warning_modal(
    screen_width, screen_height,
    "Esta acción no se puede deshacer",
    on_proceed=proceder_callback,
    on_cancel=cancelar_callback
)
```

<img width="686" height="338" alt="Captura de pantalla 2025-11-14 125523" src="https://github.com/user-attachments/assets/b450a5f0-89d5-4047-a407-2f15b354f49d" />

---

#### **6. Modal de Información**
Modal informativo con símbolo ℹ, colores azules y botón "Entendido".

```python
modal = create_info_modal(
    screen_width, screen_height,
    "Información importante del sistema",
    on_close=mi_callback
)
```

<img width="620" height="304" alt="Captura de pantalla 2025-11-14 125536" src="https://github.com/user-attachments/assets/e8ca8811-fea0-41f2-aa1c-9ca5731205e5" />

---

#### **7. Modal de Input**
Modal con campo de entrada de texto, botones "Enviar"/"Cancelar".

```python
def manejar_texto(texto_ingresado):
    print(f"Usuario escribió: {texto_ingresado}")

modal = create_input_modal(
    screen_width, screen_height,
    "Ingresa tu nombre:",
    "Escribe aquí...",
    on_submit=manejar_texto,
    on_cancel=cancelar_callback
)
```

<img width="717" height="369" alt="Captura de pantalla 2025-11-14 125549" src="https://github.com/user-attachments/assets/6e25800c-9448-4079-920a-4314e44f9449" />

---

## 💡 Ejemplos de Uso

### **Ejemplo Completo: Cambiar Solo el Color**

```python
import pygame as pg
from pygame_ui_items import *

pg.init()
screen = pg.display.set_mode((800, 600))
ui_manager = UIManager()

# MISMO código, DIFERENTES colores - ¡Así de simple!
btn1 = button_red("Eliminar", lambda: print("Eliminado"), x=100, y=100)
btn2 = button_green("Guardar", lambda: print("Guardado"), x=250, y=100)  
btn3 = button_blue("Info", lambda: print("Info"), x=400, y=100)

# Diferentes estilos, MISMO uso
btn4 = button_outline_purple("Outline", lambda: print("Outline"), x=100, y=150)
btn5 = button_gradient_orange("Gradiente", lambda: print("Gradiente"), x=250, y=150)
btn6 = button_neumorphic_pink("Neumórfico", lambda: print("Neumórfico"), x=400, y=150)

for btn in [btn1, btn2, btn3, btn4, btn5, btn6]:
    ui_manager.add_element(btn)

# Bucle principal
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

### **Ejemplo: Todos los Modales**

```python
# Función para cerrar modal
def cerrar():
    ui_manager.window_stack.pop()

# 7 modales diferentes, MISMO patrón de uso
modales = [
    create_alert_modal(800, 600, "Alerta", cerrar),
    create_confirm_modal(800, 600, "¿Confirmar?", cerrar, cerrar),
    create_error_modal(800, 600, "Error", cerrar),
    create_success_modal(800, 600, "¡Éxito!", cerrar),
    create_warning_modal(800, 600, "Advertencia", cerrar, cerrar),
    create_info_modal(800, 600, "Información", cerrar),
    create_input_modal(800, 600, "Nombre:", "Escribe...", lambda t: print(t), cerrar)
]

# Abrir cualquier modal
ui_manager.window_stack.push(modales[0])  # Alerta
```

---

## 🎯 Filosofía de Diseño

### **Simplicidad Extrema**
```python
# ❌ Antes (complejo)
button = Button(100, 100, 120, 40, "Texto", callback)
button.set_bg_color((255, 0, 0))
button.set_hover_color((200, 0, 0))
button.set_pressed_color((150, 0, 0))

# ✅ Ahora (simple)
button = button_red("Texto", callback, x=100, y=100)
```

### **Potencia en la Personalización**
```python
# Personalizar cualquier aspecto manteniendo la plantilla
button = button_blue(
    "Mi Botón", 
    callback, 
    x=100, y=100,
    width=200,           # Tamaño personalizado
    height=60,
    border_radius=20,    # Más redondeado
    font_size=24         # Texto más grande
)
```

### **Consistencia Visual**
- **12 colores** cuidadosamente seleccionados
- **4 estilos** que funcionan con todos los colores  
- **7 modales** con iconografía y colores semánticos
- **Misma API** para todas las variaciones

---

## 🚀 Ejecutar el Showcase

Para ver todas las plantillas en acción:

```bash
python example_complete_showcase.py
```

**Controles:**
- **Clic** en botones para probar estilos
- **Teclas 1-7** para abrir diferentes modales
- **ESC** para cerrar modal actual
- **Q** para salir

---

*Esta guía documenta pygame_ui_items v0.1.0 - Una librería que hace la creación de UI en Pygame tan simple como cambiar un color.*
