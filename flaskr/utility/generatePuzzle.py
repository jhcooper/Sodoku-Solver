def generate_csp(puzzle: str):
    """
    Helper function to generate a CSP representation of a puzzle. Leaves constraints empty.

    Parameters:
    - puzzle(list): A 2d list representation of the puzzle.

    Returns:
    - csp: A CSP representation of the puzzle.
    """
    csp = {"variables": {}, "constraints": {}}

    n = len(puzzle)

    # Generate variable domains
    for i in range(n):
        for j in range(n):
            variable_name = f"C{i+1}{j+1}"
            if puzzle[i][j] is None:
                csp["variables"][variable_name] = list(range(1, n + 1))
            else:
                csp["variables"][variable_name] = [puzzle[i][j]]

    return csp
