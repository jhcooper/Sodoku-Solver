from puzzles.constraints import csp


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
    unassigned = set(csp["variables"].keys()) - set(assigned.keys())

    if not unassigned:
        return False

    mrv = unassigned.pop()
    for v1 in unassigned:
        if len(domains[v1]) < len(domains[mrv]):
            mrv = v1
    return mrv


def main():
    print(minimum_remaining_values(csp, {}))


if __name__ == "__main__":
    main()
