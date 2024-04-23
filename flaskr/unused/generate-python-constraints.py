import re

def generateDict(lisp_string, filename):
    '''
    Converts 'sodoku-constraints.lisp' to a python dictionary and saves it in 'constraints.py'

    The dictionary is of the form:

    constraints = {
        ('C1', 'C2'): [(1, 2), (3, 4), ...],
        ('C2', 'C3'): [(1, 2), (3, 4), ...],
        ...
    }

    '''
    
    lisp_string = lisp_string.replace('\n', ' ').replace('\t', ' ') # remove newlines and tabs
    lisp_string = re.sub(r'\s+', ' ', lisp_string) # remove extra spaces

    # regex for variable pairs and their constraints (e.g. ((:C1 :C2) (1 2) (3 4) ...))
    group_pattern = r"\(\s*(:C\d+)\s+(:C\d+)\s*\)((?:\s*\(\d+\s+\d+\))+)" # thank you chatGPT
    # regex to match pairs of values
    pair_pattern = re.compile(r"\((\d+)\s+(\d+)\)") # compile for reuse

    constraints = {}

    # find variable pairs (e.g. (:C1 :C2)) and their constraints (e.g. (1 2) (3 4))
    for match in re.finditer(group_pattern, lisp_string):
        var_pair = (match.group(1)[1:], match.group(2)[1:]) # pair the variables
        pairs = [(int(x), int(y)) for x, y in pair_pattern.findall(match.group(0))] #generate list of pairs
        constraints[var_pair] = pairs

    # save as a python dictionary in a separate file
    with open(filename, 'w') as file:
        file.write("constraints = {\n")
        for var_pair, values in constraints.items():
            file.write(f"    {repr(var_pair)}: {values},\n")
        file.write("}\n")

lisp_constraints = open('sodoku-constraints.lisp', 'r').read()
generateDict(lisp_constraints, "constraints.py")