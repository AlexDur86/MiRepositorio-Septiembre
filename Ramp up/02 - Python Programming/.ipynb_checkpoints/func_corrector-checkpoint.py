import exercises as e

def check_ex1(func):
    """Esta funcion corrije el ejercicio 1."""

    sentences = [
        "en un lugar de la mancha",
        "ser nasi no es fasi",
        "se tu propio jefe",
        "bongo la bongo chachacha",
        "el bootcamp de data science de the bridge es el mejor",
        "el futuro sera feminista o no sera",
        "alistate en la marina"
    ]

    solutions = [
        "en un ragul de la ahcnam",
        "ser nasi no es fasi",
        "se tu oiporp jefe",
        "ognob la ognob ahcahcahc",
        "el pmactoob de data ecneics de the egdirb es el rojem",
        "el orutuf sera atsinimef o no sera",
        "etatsila en la aniram"
    ]

    fails = []
    for sentence, solution in zip(sentences, solutions):
        try:
            result = func(sentence)
            if result == solution:
                continue
            else:
                fails.append(f"La frase: '{sentence}' tiene que devolver '{solution}' y no '{result}'")

        except Exception as e:
            fails.append(f"ERROR EN CODIGO: {e}")
    
    if not len(fails):
        print("¡Ejercicio 1 esta OK! Enhorabuena :)")
    else:
        print("Revisa el ejercicio 1. Los fallos son:")
        print("\n".join(fails))


def check_ex2(func):
    """Esta funcion corrije el ejercicio 2."""

    ints = zip(
        [89, 92, 695, 46288, 2345, 2345], 
        [1, 1, 2, 3, 4, 1]
        )

    solutions = [
        1, -1, 2, 51, -1, -1
    ]

    fails = []
    for integers, solution in zip(ints, solutions):
        try:
            result = func(integers[0], integers[1])
            if result == solution:
                continue
            else:
                fails.append(f"Los enteros: '{integers}' tiene que devolver '{solution}' y no '{result}'")

        except Exception as e:
            fails.append(f"ERROR EN CODIGO: {e}")
    
    if not len(fails):
        print("¡Ejercicio 2 esta OK! Enhorabuena :)")
    else:
        print("Revisa el ejercicio 2. Los fallos son:")
        print("\n".join(fails))


def check_ex3(func):
    """Esta funcion corrije el ejercicio 3."""

    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "abcdefghijklmnopqrstuvwxyz",
        "Esta frase no"
    ]

    solutions = [
        True,
        True,
        False
    ]

    fails = []
    for sentence, solution in zip(sentences, solutions):
        try:
            result = func(sentence)
            if result == solution:
                continue
            else:
                fails.append(f"La frase: '{sentence}' tiene que devolver '{solution}' y no '{result}'")

        except Exception as e:
            fails.append(f"ERROR EN CODIGO: {e}")
    
    if not len(fails):
        print("¡Ejercicio 3 esta OK! Enhorabuena :)")
    else:
        print("Revisa el ejercicio 3. Los fallos son:")
        print("\n".join(fails))


def check_ex4(func):
    """Esta funcion corrije el ejercicio 4."""

    sentences = [
        "en un lugar de la mancha",
        "ser nasi no es fasi",
        "se tu propio jefe",
        "bongo la bongo chachacha",
        "el bootcamp de data science de the bridge es el mejor",
        "el futuro sera feminista o no sera",
        "alistate en la marina",
        "",
        "Tengo miedo a perder la maravilla de tus ojos de estatua y el acento que de noche me pone en la mejilla la solitaria rosa de tu aliento Tengo pena de ser en esta orilla tronco sin ramas"
    ]

    solutions = [
        "#EnUnLugarDeLaMancha",
        "#SerNasiNoEsFasi",
        "#SeTuPropioJefe",
        "#BongoLaBongoChachacha",
        "#ElBootcampDeDataScienceDeTheBridgeEsElMejor",
        "#ElFuturoSeraFeministaONoSera",
        "#AlistateEnLaMarina",
        False,
        False
    ]

    fails = []
    for sentence, solution in zip(sentences, solutions):
        try:
            result = func(sentence)
            if result == solution:
                continue
            else:
                fails.append(f"La frase: '{sentence}' tiene que devolver '{solution}' y no '{result}'")

        except Exception as e:
            fails.append(f"ERROR EN CODIGO: {e}")
    
    if not len(fails):
        print("¡Ejercicio 4 esta OK! Enhorabuena :)")
    else:
        print("Revisa el ejercicio 4. Los fallos son:")
        print("\n".join(fails))


def check_ex5(func):
    """Esta funcion corrije el ejercicio 5."""

    sentences = [
        "en un lugar de la mancha",
        "ser nasi no es fasi",
        "se tu propio jefe",
        "bongo la bongo chachacha",
        "el bootcamp de data science de the bridge es el mejor",
        "el futuro sera feminista o no sera",
        "alistate en la marina"
    ]

    solutions = [
        "ra ha yhtne qr yn znapun",
        "fre anfv ab rf snfv",
        "fr gh cebcvb wrsr",
        "obatb yn obatb punpunpun",
        "ry obbgpnzc qr qngn fpvrapr qr gur oevqtr rf ry zrwbe",
        "ry shgheb fren srzvavfgn b ab fren",
        "nyvfgngr ra yn znevan"
    ]

    fails = []
    for sentence, solution in zip(sentences, solutions):
        try:
            result = func(sentence)
            if result == solution:
                continue
            else:
                fails.append(f"La frase: '{sentence}' tiene que devolver '{solution}' y no '{result}'")

        except Exception as e:
            fails.append(f"ERROR EN CODIGO: {e}")
    
    if not len(fails):
        print("¡Ejercicio 5 esta OK! Enhorabuena :)")
    else:
        print("Revisa el ejercicio 5. Los fallos son:")
        print("\n".join(fails))


def check():
    check_ex1(e.ex1_graded)
    check_ex2(e.ex2_graded)
    check_ex3(e.ex3_graded)
    check_ex4(e.ex4_graded)
    check_ex5(e.ex5_graded)


if __name__ == "__main__":

    check()