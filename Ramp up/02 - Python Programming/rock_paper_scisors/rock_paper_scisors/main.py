"""Este archivo es el ejecutable del juego piedra papel o tijeras."""
import sys

import utilities.constants as c
from utilities.game_logic import game_logic
from utilities.random_play import get_computer_choice


def check_choice(human_chc):
    """Comprueba el eleccion de la persona.
    
    Comprueba que la eleccion de la persona sea valida iterativamente hasta que 
    el usuario meta un input correcto. 

    Parameters
    ----------
        human_chc str:
            String que corresponde a la eleccion del usuario.
    
    Returns
    -------
        str:
            String del usuario correcto.
    """
    human_choice = c.HUMAN_CHOICES.get(human_chc)
    if human_choice is None:
        human_choice = input(f"Por favor elige una opcion valida entre Pi, Pa, Ti: ")
        return check_choice(human_choice.capitalize())
    else:
        return human_choice


def play(human_choice):
    """Funcion principal donde se orquesta el juego.
    
    Parameters
    ----------
        human_chc str:
            String que corresponde a la eleccion del usuario.
    
    Returns
    -------
        None
    """
    keep_playing = True
    final_result = 0
    iter = 0
    while keep_playing:
        computer_choice = get_computer_choice()

        if human_choice == computer_choice:
            # Comprueba el empate
            print(f"La maquina y tu habeis elegido {computer_choice}, asi pues hay empate. Seguimos jugando.")
            human_choice = check_choice(input(f"Elige una opcion (Pi, Pa, Ti): "))
            continue

        else:
            # Ejecuta la logica del juego
            result = game_logic(human_choice, computer_choice)
            final_result += int(result)

            # Obten los resultados de la partida
            if (iter == 1) and (final_result == 2):
                print(f"¡La maquina ha ganado la partida 2-0!")
                keep_playing = False
            elif (iter == 1) and (final_result == 0):
                print(f"¡Has ganado la partida 0-2!")
                keep_playing = False
            else:
                if final_result == 2:
                    print(f"¡La maquina ha ganado la partida 2-1!")
                    keep_playing = False
                elif (iter == 2) and (final_result == 1):
                    print(f"¡Has ganado la partida 1-2!")
                    keep_playing = False
                else:
                    human_choice = check_choice(input(f"Elige una opcion (Pi, Pa, Ti): "))
                    iter += 1
                    continue


if __name__ == "__main__":
    try:
        # Intenta acceder a la posicion 1
        HUMAN_CHOICE = sys.argv[1].capitalize()
    except IndexError:
        # Si no puedes porque no se haya dado un input entonces falla y da el siguiente mensaje.
        print(f"Por favor elije una opcion entre las siguientes: Pi, Piedra, Pa, Papel, Ti, Tijeras.")
        raise
    
    # Comprueba si la eleccion es correcta y modifica si no lo es
    HUMAN_CHOICE = check_choice(HUMAN_CHOICE)

    # Ejecuta el juego
    play(HUMAN_CHOICE)
    