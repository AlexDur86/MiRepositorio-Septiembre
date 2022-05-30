"""
This is the beginning of a Python file. Here you should describe what we are
going to find in this file.

Our script is going to take 2 inputs to calculate some basic operations.
"""

# Then the imports, the libraries or functionalities that we are going to use.
import sys


# Here we can define functions to use in our script to improve the code readability
def basic_operations(a: float, b: float) -> tuple:
    """This function will perform basic operations.
    
    With this function we will do the sum and the multiplication.

    Parameters
    ----------
        a: First float used to calculate the operations.
        b: Second float used to calculate the operations.
    
    Returns
    -------
        result of the sum and multiplication.
    """
    sum = a + b
    mult = a * b
    return sum, mult


# This is the 'main' part of the file, from here Python is going to execute everything
# below the following line.
if __name__ == "__main__":
    ARG1 = sys.argv[1]  # This is how we can take the input variables
    ARG2 = sys.argv[2]
    S, M = basic_operations(float(ARG1), float(ARG2))
    print(f"{ARG1} + {ARG2} = {S}", "\n")
    print(f"{ARG1} * {ARG2} = {M}")
