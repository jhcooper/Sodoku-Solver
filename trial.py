def generate_distinct_pairs():
    # Generate all distinct pairs of digits from 1 to 9
    pairs = [(i, j) for i in range(1, 10) for j in range(1, 10) if i != j]
    return pairs

def sudoku_constraints():
    # Initialize the constraints dictionary
    constraints = {}
    # All possible rows and columns in a standard 9x9 Sudoku
    rows = '1234'
    cols = '1234'
    
    # Helper function to form box groupings
    def cross(A, B):
        return [a + b for a in A for b in B]

    # Generate all distinct value pairs
    all_pairs = generate_distinct_pairs()

    # Rows and columns constraints
    for r in rows:
        for c1 in range(len(cols)):
            for c2 in range(c1 + 1, len(cols)):
                # Row constraint between different columns
                key = (f'C{r}{cols[c1]}', f'C{r}{cols[c2]}')
                constraints[key] = all_pairs

                # Column constraint between different rows
                key = (f'C{rows[c1]}{cols[c1]}', f'C{rows[c2]}{cols[c1]}')
                constraints[key] = all_pairs

    # 3x3 square constraints
    for rs in ('12', '34'):
        for cs in ('12', '34'):
            squares = cross(rs, cs)
            for i in range(len(squares)):
                for j in range(i + 1, len(squares)):
                    key = (f'C{squares[i]}', f'C{squares[j]}')
                    if key not in constraints:
                        constraints[key] = all_pairs

    return constraints

# Generate and print the constraints for the Sudoku board
sudoku_constraints_dict = sudoku_constraints()

with open('output.txt', 'w') as file:
    for key, value in sudoku_constraints_dict.items():
        file.write(f"{key}: {value}\n")

