def minimum_remaining_values(csp: dict, assigned: dict):
    """
    Selects the variable with the minimum remaining values in its domain

    Parameters:
    - csp(dict):
        CSP representation of the sudoku board.
    - assigned(dict):
        The variables that have been assigned.

    Returns:
    - str:
        The key of the variable with the minimum remaining values in its domain.

    """
    domains = csp["variables"]
    unnassigned = [v1 for v1 in domains if v1 not in assigned]

    if not unnassigned:
        return False

    mrv = unnassigned[0]
    for v1 in unnassigned:
        if len(domains[v1]) < len(domains[mrv]):
            mrv = v1
    return mrv
