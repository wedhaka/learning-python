"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """
    text_value, coordinates = record
    return coordinates

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    tuple_coordinates = tuple(coordinate)
    return tuple_coordinates

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """
    new_coordinate = get_coordinate(azara_record)
    convert_coordinates = convert_coordinate(new_coordinate)
    vaue1, rui_coordinate, location = rui_record

    if rui_coordinate == convert_coordinates :
        return True
    return False
    
def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    is_valid = compare_records(azara_record, rui_record)

    if is_valid :
        return azara_record + rui_record
    return "not a match"

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """
    combined_all = ""
    for i, tp_values in enumerate(combined_record_group) :
        if i == 1 : 
            combined_all = combined_all + str(convert_coordinate(tp_values)) + '/n '

        combined_all = combined_all + str(tp_values) + '/n '

    return combined_all


print(clean_up((
    ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
    ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
    ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))
))