from ac3 import ac3
from revise import revise
from mrv import minimum_remaining_values
from part1 import csp as csp1
import copy

def backtrack(csp, assignment={}):
    if len(assignment) == len(csp['variables']):
        return assignment  # All variables assigned successfully

    var = minimum_remaining_values(csp, assignment)
    if not var:
        return None  # No more variables to assign, should not happen

    # Get domain values that can still be tried
    for value in csp['variables'][var]:
        if is_consistent(value, var, csp, assignment):
            assignment[var] = value
            local_csp = copy.deepcopy(csp)
            local_csp['variables'][var] = [value]  # Assign and attempt to maintain consistency

            status, ac3_csp = ac3(local_csp)  # Check arc consistency
            if status:
                result = backtrack(ac3_csp, assignment.copy())  # Recurse with a copy of assignments
                if result is not None:
                    return result  # Solution found
            del assignment[var]  # Backtrack if failed

    return None  # Trigger backtracking


def is_consistent(value, var, csp, assignment):
    """ Check if a value assignment is consistent with the assignment of other variables """
    for other_var in assignment:
        if (var, other_var) in csp['constraints']:
            if not (value, assignment[other_var]) in csp['constraints'][(var, other_var)]:
                return False
        if (other_var, var) in csp['constraints']:
            if not (assignment[other_var], value) in csp['constraints'][(other_var, var)]:
                return False
    return True


def main():
    csp = {
        'variables': {
            'A': [1],
            'B': [1, 2, 3,4],
            'C': [3, 4, 1, 2],
            'D' :[4, 1, 2,3],
        },
        'constraints': {
            ('A', 'B'): [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)],
            ('B', 'C'): [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)],
            ('C', 'A'): [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)],
            ('A', 'D'): [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)],
            ('B', 'D'): [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)],
            ('C', 'D'): [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)],
        }
    }

    print (f'\n=================SEARCHING=================\n {backtrack(csp1)}')

if __name__ == "__main__":
    main()