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
    temp = copy.deepcopy(csp)
    domains = csp["variables"]
    queue = deque(
        [(v1, v2) for v1 in csp["variables"] for v2 in csp["variables"] if v1 != v2]
    )
    while queue:
        (v1, v2) = queue.popleft()
        if revise(temp, v1, v2):
            if len(temp["variables"][v1]) == 0:
                return False, csp
            else:
                for v3 in domains.keys():
                    if (v1, v3) not in queue:
                        queue.append((v1, v3))
                    if (v3, v1) not in queue:
                        queue.append((v3, v1))
    if all(
        len(temp["variables"][d1]) != 0 for d1 in temp["variables"].keys()
    ):  # only modify csp if all domains are non-empty

        return True, temp
