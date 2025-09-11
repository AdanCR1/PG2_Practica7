# PyGameRules

PyGameRules es una librería open-source para Python que proporciona herramientas para gestionar contadores, temporizadores y estados de juego, diseñada específicamente para ser utilizada con Pygame. Esta librería es ideal para desarrolladores que buscan implementar mecánicas de juego de manera eficiente y modular.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Características](#características)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Referencia de la API](#referencia-de-la-api)
- [Pautas de Contribución](#pautas-de-contribución)
- [Licencia](#licencia)


## Instalación
Puedes instalar PyGameRules usando pip:

```bash
pip install PyGameRules
```

Asegúrate también de tener Pygame instalado. Puedes instalarlo usando:

```bash
pip install pygame
```

---

## Características

- **Contadores Inteligentes**: Maneja vidas, puntos y recursos con validación automática de rangos y eventos personalizables.
- **Temporizadores Precisos**: Implementa cooldowns, delays y timers sincronizados con el loop de Pygame, soportando callbacks y reutilización.
- **Máquina de Estados**: Sistema robusto para gestionar estados de juego (ej: pausa, menú, juego, game over) con transiciones seguras y callbacks.
- **Sistema de Eventos**: Permite definir, suscribir y disparar eventos personalizados con prioridad y datos asociados.
- **Patrones de Diseño**: Uso de Builder, Factory, Singleton y Observer para máxima flexibilidad y mantenibilidad.
- **Compatible con Pygame**: Integración perfecta con el ciclo principal de Pygame y fácil de incorporar en proyectos existentes.

---

## Ejemplos de Uso

### 1. Contadores

#### Contador Básico

```python
from pygame_rules.counters import Counter

score = Counter()
score.increment()
print(score.get_value())  # Salida: 1
score.decrement()
print(score.get_value())  # Salida: 0
score.set_value(10)
print(score.get_value())  # Salida: 10
score.reset()
print(score.get_value())  # Salida: 0
```

#### Contador con Rango y eventos

```python
def on_change(value):
    print(f"Nuevo valor: {value}")

def on_max():
    print("¡Valor máximo alcanzado!")

def on_min():
    print("¡Valor mínimo alcanzado!")

lives = Counter(min_value=0, max_value=5, initial=3)
lives.on_change = on_change
lives.on_max_reached = on_max
lives.on_min_reached = on_min

lives.increment(2)  # Nuevo valor: 5, ¡Valor máximo alcanzado!
lives.decrement(5)  # Nuevo valor: 0, ¡Valor mínimo alcanzado!
```

#### Contador Global (Singleton)

```python
from pygame_rules.counters import Counter

global_counter = Counter.global_instance()
global_counter.increment()
```

### 2. Temporizadores Precisos

#### Temporizador Countdown

```python
from pygame_rules.timers import Timer

def on_timer_complete():
    print("¡Tiempo terminado!")

timer = Timer(duration=3, callback=on_timer_complete)
timer.start()

# En el loop principal de Pygame:
while timer.is_running:
    timer.update()  # Llama a update() en cada frame
```

#### Temporizador con Pausa y Reanudación

```python
timer = Timer(duration=10)
timer.start()
# ... después de algunos segundos
timer.pause()
# ... luego
timer.resume()
```

#### Cooldown Reutilizable

```python
cooldown = Timer(duration=2, auto_reset=True)
cooldown.start()
# En cada frame:
cooldown.update()
if not cooldown.is_running:
    print("Cooldown listo para reutilizar")
    cooldown.start()
```

### 3. Máquina de Estados

```python
from pygame_rules.states import StateMachine, State

def on_enter_play():
    print("Entrando a PLAY")

def on_exit_play():
    print("Saliendo de PLAY")

state_machine = StateMachine()
state_machine.add_state(State("MENU"))
state_machine.add_state(State("PLAY", on_enter=on_enter_play, on_exit=on_exit_play))
state_machine.add_state(State("PAUSE"))
state_machine.add_state(State("GAME_OVER"))

state_machine.change_state("PLAY")   # Entrando a PLAY
state_machine.change_state("PAUSE")  # Saliendo de PLAY
```

#### Stack de Estados (pausa y reanudación)

```python
from pygame_rules.states import StateMachine, State

state_machine = StateMachine()
state_machine.add_state(State("MENU"))
state_machine.add_state(State("PLAY"))
state_machine.add_state(State("PAUSE"))
state_machine.add_state(State("GAME_OVER"))

state_machine.change_state("PLAY")
state_machine.change_state("PAUSE")
```

### 4. Sistema de Eventos

```python
from pygame_rules.event_system import EventSystem

def on_custom_event(data):
    print(f"Evento recibido con datos: {data}")

event_system = EventSystem()
event_system.subscribe("powerup_collected", on_custom_event)
event_system.emit("powerup_collected", {"type": "vida", "valor": 1})
```

#### Evento con Prioridad

```python
def high_priority(data):
    print("Alta prioridad")

def low_priority(data):
    print("Baja prioridad")

event_system.subscribe("evento", low_priority, priority=10)
event_system.subscribe("evento", high_priority, priority=1)
event_system.emit("evento", {})
# Salida: Alta prioridad \n Baja prioridad
```

## Referencia de la API

- **Counter**: Clase para gestionar contadores.
  * increment(amount=1)
  * decrement(amount=1)
  * set_value(value)
  * get_value()
  * set_max_value(max_value)
  * set_min_value(min_value)
  * events: on_change, on_max_reached, on_min_reached
  
- **Timer**: Clase para gestionar temporizadores.
  * start(duration, callback=None)
  * stop()
  * pause()
  * resume()
  * update()
  * is_running()
  * is_paused()
  * set_callback(callback)
  
- **StateMachine**: Clase para gestionar estados del juego.
  * add_state(state: State)
  * change_state(name: str)
  * push_state(state_name: str)
  * pop_state()
  * get_current_state()
  * callbacks: on_enter, on_exit, on_update

- **EventSystem**: Clase para gestionar eventos personalizados.
  * subscribe(event_name, priority=100)
  * unsubscribe(event_name, callback)
  * emit(event_name, data)

## Pautas de Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'feat: Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.