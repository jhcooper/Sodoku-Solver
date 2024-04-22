def revise(csp, v1, v2):
    """
    Remove values from v1's domain that are not consistent with v2's domain.
    """
    revised = False
    # print(f'revising ({v1}, {v2})')
    d1 = csp['variables'].get(v1)
    # print(f'D1: {d1}')
    d2 = csp['variables'].get(v2)
    # print(f'D2: {d2}')

    constraints = csp['constraints'].get((v1,v2),[])
    if not constraints:
        constraints = csp['constraints'].get((v2,v1),[])
        if not constraints:
            # print (f"no constraint exists for ({v1}, {v2}) ")
            return revised
        constraints = [(y,x) for (x,y) in constraints]
    for x in d1:
        if not (any((x,y) in constraints for y in d2)):
            d1.remove(x)
            revised = True

    csp['variables'][v1] = d1
    # print (f'New D1: {csp["variables"][v1]}')
    return revised



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
    x = 'B'
    y = 'C'

    print (f'\n=================REVISING {x} and {y}=================\n {revise(csp, x, y)}')

if __name__ == "__main__":
    main()