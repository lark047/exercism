"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
LAYER_PREP_TIME = 2

def bake_time_remaining(bake_time_elapsed):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return max(EXPECTED_BAKE_TIME - bake_time_elapsed, 0)

def preparation_time_in_minutes(number_of_layers):
    """Calcuate the prep time based on the number of layers

    Parameters:
        number_of_layers (int): The desired number of layers

    Returns:
        int: The total preparation time for `number_of_layers` layers

    Function that takes the desired layers in the lasagna as an argument
    and returns the total prep time in minutes
    """
    return number_of_layers * LAYER_PREP_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total prep + bake time

    Paramaters:

    Returns:

    Function that takes the desired number of layers and time the
    lasagna has already spent in the oven and returns the total 
    prep + bake time
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
