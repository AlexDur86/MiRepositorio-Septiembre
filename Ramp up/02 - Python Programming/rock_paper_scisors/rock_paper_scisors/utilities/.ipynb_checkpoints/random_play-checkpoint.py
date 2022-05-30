"""En este archivo se encuentran las funcionalidades para la eleccion aleatoria del ordenador."""
import random

from utilities import constants as c


def get_computer_choice():
    """Funcion para que el ordenador elija una opcion."""
    return random.choice(c.CHOICES)