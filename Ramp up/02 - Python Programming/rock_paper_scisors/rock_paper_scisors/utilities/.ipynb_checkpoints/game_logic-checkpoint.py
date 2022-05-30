"""En este archivo se encuentra la logica del juego."""
from utilities import constants as c


def game_logic(human, computer):
    """Funcion que computa la logica del juego.
    
    ## AQUI DOCUMENTARIAMOS LA LOGICA DEL JUEGO ##
    
    Parameters
    ----------
        human str:
            Eleccion del usuario.
        
        computer str:
            Eleccion del ordenador.
    
    Returns
    -------
        bool:
            True si la maquina gana la partida, False si gana el usuario.
    """
    if human == c.CHOICES[0]:
        if computer == c.CHOICES[1]:
            ret = True
            print(f"¡Ha ganado la maquina! {computer} gana a {human}")
        else:
            ret = False
            print(f"¡Has ganado! {human} gana a {computer}")
    
    elif human == c.CHOICES[1]:
        if computer == c.CHOICES[0]:
            ret = True
            print(f"¡Ha ganado la maquina! {computer} gana a {human}")
        else:
            ret = False
            print(f"¡Has ganado! {human} gana a {computer}")
    else:
        if computer == c.CHOICES[0]:
            ret = True
            print(f"¡Ha ganado la maquina! {computer} gana a {human}")
        else:
            ret = False
            print(f"¡Has ganado! {human} gana a {computer}")
    return ret
