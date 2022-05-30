"""en este archivo están los ejercicios evaluables de Iñigo Fuertes Sierra."""


def ex1_graded(sentence):
    """Invierte el orden de los caracteres de las palabras con largo de más de 5 caracters.
    
    Parametros
    ----------
        sentence str
           frase a invertir
    Returns
    -------
        Lista:
            lista con las palabras del parametro incial con las palabras de mas de 5 caracteres invertidas.
    """
    sent = sentence.split(" ")
    sent2 = []
    for word in sent:
        if len(word) >= 5:
            sent2.append(word[::-1])
        else:
            sent2.append(word)
    return " ".join(sent2)


def ex2_graded(numero, pot):
    """It separates "n" into digits, and raises them to p + 1 for each iteration of the code.
    
    Parametros
    ----------
        numero int
          numero a separar en digitos
        pot int
            potencia por la que se mepieza a elevar
    Returns
    -------
        Lista:
            r_t int
             en caso de existir numero que genere resto = 0 y -1 en caso de no exisitir
    """
    num = str(numero)
    suma = sum([int(num[i]) ** (pot + i) for i in range(len(num))])
    
    if suma % numero == 0:
        r_t = suma/numero
    else: 
        r_t = -1
    return r_t


def ex3_graded(frase): 
    """Comprueba que la frase contenga al menos una vez todas las letras del alfabeto.
    
    Parametros
    ----------
        frase str
            frase a detectar si contiene todas las letras
    Returns
    -------
        Boolean:
            True si contiene todas las letras, False si no contiene todas las letras
    """
    frase = frase.lower()
    frase = set(frase)
    
    num_let = [letter for letter in frase if ord(letter) in range(ord('a'), ord('z')+1)] 
  
    if len(num_let) == 26: 
        return True
    else: 
        return False


def ex4_graded(mkt_phrase):
    """Genera hastags a partiendo de una frase dada cumpliendo unas coniciones delongitud y de estilo de escritura.
    
    Parametros
    ----------
        mkt_phrase str
            frase a convertir en hastag
            
    Returns
    -------
        rt str:
           frase con las condiciones cumplidas
    """
    mkt_hs = mkt_phrase.strip() 
    if len(mkt_hs) == 0 or len(mkt_hs) > 140:
        r_t = False
    else:
        r_t = (f"#{mkt_hs.title().replace(' ','')}")
    return r_t


def ex5_graded(frase):
    """Cambia cada carcater dde una frase por un equivalente al sumarle 13 en su posicion en el alfabeto.
    
    Parametros
    ----------
        frase str
            frase a cambiar sus caracteres 
            
    Returns
    -------
        rt str:
          frase los carcateres cambiados
    """
    frase_ = frase.lower()
    prim = "abcdefghijklm"
    sec = "nopqrstuvwxyz"
    mapeo_letras = dict(zip(prim+sec, sec+prim))
    return "".join(mapeo_letras.get(_, _) for _ in frase_)
