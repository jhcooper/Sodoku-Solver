from constraints import constraints
from figure3 import csp as csp2
from part1 import csp as csp3
"""
Write a function revise that takes a CSP such as the one in Figure 3 (or what you defined in
Part 1) and the names of two variables as input and modifies the CSP, removing any value in the
first variable’s domain where there isn’t a corresponding value in the other variable’s domain that
satisfies the constraint between the variables. The function should return a boolean indicating
whether or not any values were removed.
"""

csp1 = {
'variables' : {
'C1' : [1],
"C2" : [1,2,3],
"C3" : [2],},

'constraints' : {('C1', 'C2') : 
              [(1,2),
               (2,1),
               (1,3),
               (3,1),
               (2,3),
                (3,2)],
               ('C2', 'C3') :
               [(1,2),
               (2,1),
               (1,3),
               (3,1),
               (2,3),
                (3,2)],
                ('C1', 'C3') :
                [(1,2),
                 (2,1),
                 (1,3),
                 (3,1),
                 (2,3),
                  (3,2)]}

}




def minimum_remaining_values(csp, assignments):
    print("Calculating MRV")
    variables = csp['variables']
    unassigned = [var for var in variables if var not in assignments]
    if not unassigned:
        print("No unassigned variables left")
        return None
    mrv = unassigned[0]
    for var in unassigned:
        if len(variables[var]) < len(variables[mrv]):
            mrv = var
    print(f"Variable with minimum remaining values: {mrv} with domain {csp['variables'][mrv]}")
    return mrv
import copy

def revise(csp, v1, v2):
    """ Remove values from v1's domain that are not consistent with v2's domain. """
    revised = False
    changes = []
    constraints = csp['constraints'].get((v1, v2), [])
    if not constraints:
        constraints = csp['constraints'].get((v2, v1), [])
        if not constraints:
            return False, changes
        constraints = [(y, x) for (x, y) in constraints]

    for x in csp['variables'][v1][:]:  # Iterate over a copy of the domain
        if not any((x, y) in constraints for y in csp['variables'][v2]):
            csp['variables'][v1].remove(x)
            changes.append((v1, x))
            revised = True

    return revised, changes

def ac3(csp, queue=None):
    """ Propagate constraints and reduce domains using the AC-3 algorithm. """
    changes = []
    if queue is None:
        queue = [(key[0], key[1]) for key in csp['constraints']] + [(key[1], key[0]) for key in csp['constraints']]

    while queue:
        (v1, v2) = queue.pop(0)
        revised, local_changes = revise(csp, v1, v2)
        changes.extend(local_changes)
        if revised:
            if len(csp['variables'][v1]) == 0:
                return False, changes
            for v3 in csp['variables']:
                if v3 != v1 and v3 != v2:
                    queue.append((v3, v1))

    return True, changes

def backtrack(csp, assignments, order, failed_values, backtrack_counts, remaining_unassigned):
    """ Perform a backtracking search to find a solution for the CSP. """
    if len(assignments) == len(csp['variables']):
        return True  # Solution found

    var = minimum_remaining_values(csp, assignments)
    if not var:
        return False  # No viable variable to assign, backtrack

    original_domains = copy.deepcopy(csp['variables'])  # Deep copy of domains

    for value in csp['variables'][var]:
        assignments[var] = value
        order.append(var)
        success, changes = ac3(csp)  # Propagate constraints

        if success:
            result = backtrack(csp, assignments, order, failed_values, backtrack_counts, remaining_unassigned)
            if result:
                return result

        # Undo changes: remove assignment and restore domains
        del assignments[var]
        order.pop()
        failed_values[var].append(value)
        backtrack_counts[var] += 1
        for v, val in changes:
            csp['variables'][v].append(val)  # Restore the removed value

    csp['variables'] = original_domains  # Restore all domains from backup
    return False

def backtracking_search(csp):
    """ Initialize and start the backtracking search. """
    assignments = {}
    order = []
    failed_values = {var: [] for var in csp['variables']}
    backtrack_counts = {var: 0 for var in csp['variables']}
    remaining_unassigned = {k: v[:] for k, v in csp['variables'].items() if k not in assignments}
    if backtrack(csp, assignments, order, failed_values, backtrack_counts, remaining_unassigned):
        return assignments, order, failed_values, backtrack_counts, remaining_unassigned
    return None

# Assuming `csp` is defined elsewhere and passed to this function

def main():
    Csp = {
        'variables': {
            'A': [1],
            'B': [1, 2, 3,4],
            'C': [3],
            'D' :[4],
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
    csp = csp3
    # print ("Testing Ac3")
    # print(ac3(csp))
    print("Testing Backtracking Search")
    assignments, order, failed_values, backtrack_counts, remaining_unassigned = backtracking_search(csp)
    print(f"\n=====================\nAssignments\n======================\n{assignments}")
    print(f"\n=====================\nOrder\n======================\n{order}")
    print(f"\n=====================\nFailed Values\n======================\n{failed_values}")
    print(f"\n=====================\nBacktrack Counts\n======================\n{backtrack_counts}")
    print(f"\n=====================\nRemaining Unassigned\n======================\n{remaining_unassigned}")

    

    

if __name__ == "__main__":
    main()




# print(f'revising C1 and C2: {revise(csp, "C1", "C2")}')
# print(f'csp after revising C1 and C2: {csp["variables"]}\n')
# print(f'revising C1 and C3: {revise(csp, "C1", "C3")}')
# print(f'csp after revising C1 and C3: {csp["variables"]} \n')
# print(f'revising C2 and C3: {revise(csp, "C2", "C3")}')
# print(f'csp after revising C2 and C3: {csp["variables"]}\n')
# print(f'revising C2 and C1: {revise(csp, "C2", "C1")}')
# print(f'csp after revising C2 and C1: {csp}')
# print(f'revising C3 and C1: {revise(csp, "C3", "C1")}')
# print(f'csp after revising C3 and C1: {csp["variables"]}\n')