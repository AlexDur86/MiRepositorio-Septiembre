"""En este archivo se encuentran las constantes del juego."""

# Esta variable indica la opciones que el ordenador puede escoger.
CHOICES = [
    "Piedra", "Papel", "Tijeras"
]

# Esta variable indica las opciones que el usuario tiene permitido elegir.
HUMAN_CHOICES = {
    "Ti": "Tijeras",
    "Tijeras": "Tijeras",
    "Pa": "Papel",
    "Papel": "Papel",
    "Pi": "Piedra",
    "Piedra": "Piedra"
}