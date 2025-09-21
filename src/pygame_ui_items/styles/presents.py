from typing import Dict, Any

def get_preset_styles(preset_name: str) -> Dict[str, Any]:
    """Obtiene estilos predefinidos por nombre"""
    presets = {
        "rounded": {
            "border_radius": 15,
            "padding": (20, 10)
        },
        "minimal": {
            "border_radius": 0,
            "border_width": 0,
            "padding": (15, 8)
        },
        "outlined": {
            "border_radius": 8,
            "border_width": 2,
            "bg_color": (255, 255, 255),
            "text_color": (0, 0, 0),
            "border_color": (0, 123, 255),
            "hover_bg_color": (240, 240, 240),
        },
        "gradient": {
            "border_radius": 10,
            # Nota: La implementación de gradiente iría en el drawing
        }
    }
    return presets.get(preset_name, {})