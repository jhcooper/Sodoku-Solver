from revise import revise
from part1 import csp
def ac3(csp):
    temp = csp.copy()
    domains = csp['variables']
    queue = [(v1, v2) for v1 in domains.keys() for v2 in domains.keys()]
    while queue:
        (v1, v2) = queue.pop(0)
        if (revise(temp, v1, v2)):
            if len(temp['variables'][v1]) == 0:
                return False, csp
            else:
                for v3 in domains.keys():
                    if ((v1,v3) not in queue):
                        queue.append((v1,v3))
                    if ((v3,v1) not in queue):
                        queue.append((v3,v1))
    if (len(temp['variables'][d1]) != 0 for d1 in temp['variables'].keys()):
        
        return True, temp


def main():

    print (f'CSP before: {csp}\n')
    print (f'\n=================AC3=================\n {ac3(csp)}\n=================+++=================\n')
    print(f'CSP After: {csp}')


if __name__ == "__main__":
    main()


