from ac3 import ac3
from mrv import minimum_remaining_values
import copy


def backtrack(
    csp, assignment={}, order=[], to_assign={}, failed=None, prev=None, steps=[]
):
    """
    Backtracking search that solves a sudoku board given it's CSP representation

    Parameters:

    - csp(dict):
        CSP representation of the sudoku board.
    - assignment(dict):
        stores the current assignment of each assigned square.
    - order(list):
        Stores the order of assignment of tiles.
    - to_assign(dict):
        The domain of each unassigned variables.
    - failed(dict):
        Stores the failed values for each variable.
    - prev(dict):
        Stores the number of times a variable has been backtracked.
    - steps(list):
        Stores the state of the board at each step.
            step: str
                The type of step. Either assign or backtrack.
            var: str
                The variable that was assigned or backtracked.
            value: int
                The value that was assigned or backtracked.
            state: dict
                The state of the board at that step.

    Returns: Same as the input parameters.
    """
    if failed is None:
        failed = {var: [] for var in csp["variables"]}
    if prev is None:
        prev = {var: 0 for var in csp["variables"]}

    if len(assignment) == len(csp["variables"]):
        return assignment, order, to_assign, failed, prev, steps

    var = minimum_remaining_values(csp, assignment)
    if not var:
        return None

    for value in csp["variables"][var]:
        if is_consistent(value, var, csp, assignment):
            assignment[var] = value
            order.append(var)
            to_assign[var] = unassigned_domain(csp, assignment)
            local_csp = copy.deepcopy(csp)
            local_csp["variables"][var] = [value]
            steps.append(
                {
                    "step": "assign",
                    "var": var,
                    "value": value,
                    "state": copy.deepcopy(assignment),
                }
            )

            status, ac3_csp = ac3(local_csp)
            if status:
                result = backtrack(
                    ac3_csp, assignment.copy(), order, to_assign, failed, prev, steps
                )
                if result is not None:
                    return result

            failed[var].append(value)
            prev[var] += 1
            del assignment[var]
            order.pop()
            steps.append(
                {
                    "step": "backtrack",  # meant for visualizing for the fancy version, doesn't work
                    "var": var,
                    "value": value,
                    "state": copy.deepcopy(
                        assignment
                    ),  # used to track board state at each step
                }
            )

    return None


def unassigned_domain(csp, assignment):
    """
    Helper function to get the domains of all unassigned variables

    Parameters:
    - csp(dict):
        CSP representation of the sudoku board.
    - assignment(dict):
        stores the current assignment of each assigned square.

    Returns:
    - dict:
        Dictionary containing the domains of all unassigned variables.
    """
    unassigned = set(csp["variables"].keys()) - set(assignment.keys())
    return {var: csp["variables"][var] for var in unassigned}


def is_consistent(val, v1, csp, assignment):
    """
    Helper function to check if a value assignment is consistent with the constraints.
    Essentially Revise without removing values.

    Parameters:
    - value(int):
        The value to be assigned to the variable.
    - var(str):
        The variable to be assigned.
    - csp(dict):
        CSP representation of the sudoku board.
    - assignment(dict):
        stores the current assignment of each assigned square.

    Returns:
    - bool:
        True if the value assignment is consistent with the constraints, False otherwise.

    """
    # Check bidirectional constraints
    for v2 in assignment:
        if (v1, v2) in csp["constraints"]:
            if not (val, assignment[v2]) in csp["constraints"][(v1, v2)]:
                return False
        if (v2, v1) in csp["constraints"]:
            if not (assignment[v2], val) in csp["constraints"][(v2, v1)]:
                return False
    return True
