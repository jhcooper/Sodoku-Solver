from part1 import csp as csp1
def minimum_remaining_values(csp: dict, assigned: dict):
    domains = csp['variables']
    unnassigned = [v1 for v1 in domains if v1 not in assigned]
    if not unnassigned: 
        return False
    
    mrv = unnassigned[0]
    for v1 in unnassigned:
        if len(domains[v1]) < len(domains[mrv]):
            mrv = v1
    return mrv


def main():
    csp = {
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
    # assigned = {}

    assigned = {
        'A',
        'C',
        'D',
    }

    print (f'\n=================MRV=================\n {minimum_remaining_values(csp1, assigned)}')

if __name__ == "__main__":
    main()