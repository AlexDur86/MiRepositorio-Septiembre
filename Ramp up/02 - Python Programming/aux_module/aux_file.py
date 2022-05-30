"""
This file is an auxiliary file to help in the subject 07_modules.
"""


def mean_function(l):
    """Calculate the mean of a given list of numbers.
    
    First check that all elements in the list are numbers
    and then calculate the sum and the length of the vector
    to deploy the mean.
    
    Parameters
    ----------
        l list:
            List of numbers to deploy the mean.
            
    Returns
    -------
        float:
            Float number corresponding with the mean of the
            given list.
    """
    is_all_elements_numbers = all(True if (isinstance(e, int) or isinstance(e, float)) else False for e in l)
    if not is_all_elements_numbers:
        raise Exception("Check argument l because not all elements are numbers")
    else:
        s = sum(l)
        length = len(l)
        return s / length
