"""Ejercicios realizados por Alejandro Durán Rodríguez."""


def ex1_graded(sentence):
    """Reverses the character order of words longer than 5 characters.

    Parameters
    ----------
        sentence str:
            given sentence 

    Returns
    -------
        list:
            all words bigger than 5 letters will be reverse and less 5 letters will be the same.        
    """
    return " ".join([i[::-1] if len(i) >= 5 else i for i in sentence.split(" ")])   


def ex2_graded(num_str, num_int):
    """Separate "num_str" into digits, and raises them to num_int + 1 for each iteration of the code.
    
    Parameters
    ----------
        num_str:
         number to separate into digits
        num_int:
         power by which it starts to rise

    Returns
    -------
        int:
        in case of exist number that generates remainder = 0 and -1 in case of not exist
    """
    str_num = str(num_str)
    total = 0
    for i in str_num:
        total += pow(int(i), num_int)
        num_int += 1
    if total % num_str == 0:
        return total // num_str
    else:
        return -1


def ex3_graded(string):
    """Check that the sentence contains at least once all the letters of the alphabet.
    
    Parameters
    ----------
        sentence str:
            phrase to detect if it contains all the letters 
    
    Returns
    -------
        Boolean:
            True if the phrase is a pangram, False if not.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in string.lower():
            return False
    return True
 

def ex4_graded(sentence):
    """Generate hastags starting from a given sentence, fulfilling the length and writing style conditions.
    
    Parameters
    ----------
        sentence str:
            given sentence to convert in hashtag
    
    Returns
    -------
        str:
         a join sentence with "#" in the first element
    """
    return "#" + "".join([i.strip().title() for i in sentence.split()]) if 140 > len(sentence) > 1 else False
    
    
def ex5_graded(string):
    """Change each character of a phrase for an equivalent by adding 13 to its position in the alphabet.
    
    Parameters
    ----------
        str string:
            given sentence to change characters
    
    Returns
    -------
        str:
         sentence translate to ROT13 code
    """
    ordinary_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rot_13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

    return string.translate(string.maketrans(ordinary_alphabet, rot_13))