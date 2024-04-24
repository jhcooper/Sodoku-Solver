from revise import revise
import copy
from collections import deque


def ac3(csp):
    """
    AC3 algorithm for Solving Sudoku CSP. Returns the modified CSP if it is arc consistent, otherwise returns the original CSP.

    Parameters:
    - csp(dict):
        CSP representation of the sudoku board.

    Returns:
    - bool:
        True if the CSP is arc consistent, False otherwise.
    - dict:
        The modified CSP if the CSP is arc consistent, otherwise the original CSP.
    """
    domains = csp["variables"]
    queue = deque(
        [(v1, v2) for v1 in csp["variables"] for v2 in csp["variables"] if v1 != v2]
    )
    arc_consistent = True
    while queue:
        (v1, v2) = queue.popleft()
        if revise(csp, v1, v2):
            if len(domains[v1]) == 0:
                arc_consistent = False
                break
            else:
                for v3 in (v for v in domains if v != v1):
                    if (v3, v1) not in queue:
                        queue.append((v3, v1))
    return arc_consistent
