import sys
import random

if __name__ == "__main__":
    pass




def piedra_papel_tijera():
    
    x = 3
    while x > 0:
        pc = random.choice(["piedra", "pi", "tijera", "ti", "papel", "pa"])
        jugador = input("Elija una opción: ").lower()
    
        if jugador == "piedra" or jugador == "pi":
            if pc == "piedra" or pc == "pi":
                print("El ordenador elige piedra, Empate!")
                continue
            elif pc == "papel" or pc == "pa":
                print("El ordenador elige papel, pierdes")
                x -= 1
            elif pc == "tijera" or pc == "ti":
                print("El ordenador elije tijera, ganas")
                x -= 1
                
        elif jugador == "tijera" or jugador == "ti":
            if pc == "piedra" or pc == "pi":
                print("El ordenador elige piedra, pierdes")
                x -= 1
            elif pc == "papel" or pc == "pa":
                print("El ordenador elige papel, ganas")
                x -= 1
            elif pc == "tijera" or pc == "ti":
                print("El ordenador elije tijera, empate!")
                continue
                
        elif jugador == "papel" or jugador == "pa":
            if pc == "piedra" or pc == "pi":
                print("El ordenador elige piedra, ganas")
                x -= 1
            elif pc == "papel" or pc == "pa":
                print("El ordenador elige papel, empate")
                continue
            elif pc == "tijera" or pc == "ti":
                print("El ordenador elije tijera, pierdes")
                x -= 1
                
        else:
            print("Introduzca una opción valida")
            



        



