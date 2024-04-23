from ac3 import ac3
from revise import revise
from mrv import minimum_remaining_values
from part1 import csp as csp1
from constraints import csp as csp2
import copy


def backtrack(csp, assignment={}, order=[], to_assign={}, failed=None, prev=None):
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

    Returns: Same as the input parameters.
    """
    if failed is None:
        failed = {var: [] for var in csp["variables"]}
    if prev is None:
        prev = {var: 0 for var in csp["variables"]}

    if len(assignment) == len(csp["variables"]):
        return (
            assignment,
            order,
            to_assign,
            failed,
            prev,
        )

    var = minimum_remaining_values(csp, assignment)
    if not var:
        return None  # No more variables to assign, shouldn't happen

    for value in csp["variables"][var]:
        if is_consistent(
            value, var, csp, assignment
        ):  # Precheck Consistency to save on time and computation
            assignment[var] = value
            local_csp = copy.deepcopy(csp)
            local_csp["variables"][var] = [value]
            order.append(var)
            to_assign[var] = unassigned_domain(csp, assignment)

            status, ac3_csp = ac3(local_csp)  # Check arc consistency
            if status:
                result = backtrack(
                    ac3_csp, assignment.copy(), order, to_assign, failed, prev
                )
                if result is not None:
                    return result  # Solution found

            # If ac3 fails, backtrack
            failed[var].append(value)
            prev[var] += 1
            del assignment[var]
            order.pop()

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


def main():
    csp = {
        "variables": {
            "A": [1],
            "B": [1, 2, 3, 4],
            "C": [3, 4, 1, 2],
            "D": [4, 1, 2, 3],
        },
        "constraints": {
            ("A", "B"): [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 3),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 4),
                (4, 1),
                (4, 2),
                (4, 3),
            ],
            ("B", "C"): [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 3),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 4),
                (4, 1),
                (4, 2),
                (4, 3),
            ],
            ("C", "A"): [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 3),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 4),
                (4, 1),
                (4, 2),
                (4, 3),
            ],
            ("A", "D"): [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 3),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 4),
                (4, 1),
                (4, 2),
                (4, 3),
            ],
            ("B", "D"): [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 3),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 4),
                (4, 1),
                (4, 2),
                (4, 3),
            ],
            ("C", "D"): [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 3),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 4),
                (4, 1),
                (4, 2),
                (4, 3),
            ],
        },
    }
    failed = {var: [] for var in csp2["variables"]}
    prev = {var: 0 for var in csp2["variables"]}

    print("\n=================SEARCHING=================\n")
    assignment, order, to_assign, failed, prev = backtrack(csp2)
    print(f"=================Assignment=================\n {assignment}\n")
    print(f"=================Order=================\n {order}\n")
    print(f"=================To Assign=================\n {to_assign}\n")
    print(f"=================Failed=================\n {failed}\n")
    print(f"=================Prev=================\n {prev}\n")


if __name__ == "__main__":
    main()
