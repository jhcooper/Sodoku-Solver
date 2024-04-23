def parse_string(input_string):
    """
    Helper function to parse a string representation of a puzzle into a 2d list.

    Parameters:
    - input_string(str): The string representation of the puzzle. ((row1)(row2)...(rowN) where each row is a space separated list of integers or nil)

    Returns:
    - list: A 2d list representation of the puzzle.
    """
    # Generates a 2d list from a string representation of a puzzle

    # Remove all parentheses and newlines
    input_string = input_string.replace("(", "").replace(")", "")

    # Split the string into a list of strings
    input_list = input_string.split("\n")
    # Remove all empty strings
    input_list = [x for x in input_list if x]

    ret = []
    for row in input_list:
        ret.append([int(x) if x != "nil" else None for x in row.split()])

    return ret
