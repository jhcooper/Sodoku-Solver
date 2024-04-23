def revise(csp, v1, v2):
    """
    Removes values from v1's domain that are not consistent with v2's domain.

    Parameters:
    - csp(dict):
        CSP representation of the sudoku board.
    - v1(str):
        The first variable.
    - v2(str):
        The second variable.

    Returns:
    - bool:
        True if the domain of v1 is revised, False otherwise.

    """
    revised = False
    d1 = csp["variables"].get(v1)
    d2 = csp["variables"].get(v2)

    constraints = csp["constraints"].get((v1, v2), [])
    if not constraints:
        constraints = csp["constraints"].get((v2, v1), [])
        if not constraints:
            return revised
        constraints = [(y, x) for (x, y) in constraints]
    for x in d1:
        if not (
            any((x, y) in constraints for y in d2)
        ):  # if there is no value in d2 that satisfies the constraint with x
            d1.remove(x)  # modify the domain of v1 directly
            revised = True

    return revised


def main():
    csp = {
        "variables": {
            "A": [1],
            "B": [1, 2, 3, 4],
            "C": [3],
            "D": [4],
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
    x = "B"
    y = "C"

    print(
        f"\n=================REVISING {x} and {y}=================\n {revise(csp, x, y)}"
    )


if __name__ == "__main__":
    main()
