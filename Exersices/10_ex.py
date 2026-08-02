"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    return [i + number for i in range(3)]

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.
    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.
    Returns:
        list:  All rounds played.
    """
    return rounds_1 + rounds_2
    