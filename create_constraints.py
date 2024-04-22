def create_sudoku_csp(board):
    csp = {'variables': {}, 'constraints': []}

    n = len(board)  # Sudoku size, typically 9x9

    # Initialize variable domains
    for r in range(n):
        for c in range(n):
            var = (r, c)
            if board[r][c] == 'nil':
                csp['variables'][var] = list(range(1, 10))
            else:
                csp['variables'][var] = [board[r][c]]

    # Define constraints
    def add_all_different_constraint(variables):
        for i in range(len(variables)):
            for j in range(i + 1, len(variables)):
                csp['constraints'].append((variables[i], variables[j]))

    # Row and column constraints
    for i in range(n):
        row_vars = [(i, j) for j in range(n)]
        col_vars = [(j, i) for j in range(n)]
        add_all_different_constraint(row_vars)
        add_all_different_constraint(col_vars)

    # Block constraints
    block_size = int(n ** 0.5)
    for block_row in range(0, n, block_size):
        for block_col in range(0, n, block_size):
            block_vars = [(i, j) for i in range(block_row, block_row + block_size)
                           for j in range(block_col, block_col + block_size)]
            add_all_different_constraint(block_vars)

    return csp

# Example Sudoku start state as a 2D tuple array
sudoku_board = (
    (1, 'nil', 'nil', 2, 'nil', 3, 8, 'nil', 'nil'),
    ('nil', 8, 2, 'nil', 6, 'nil', 1, 'nil', 'nil'),
    (7, 'nil', 'nil', 'nil', 'nil', 1, 6, 4, 'nil'),
    (3, 'nil', 'nil', 'nil', 9, 5, 'nil', 2, 'nil'),
    ('nil', 7, 'nil', 'nil', 'nil', 'nil', 'nil', 1, 'nil'),
    ('nil', 9, 'nil', 3, 1, 'nil', 'nil', 'nil', 6),
    ('nil', 5, 3, 6, 'nil', 'nil', 'nil', 'nil', 1),
    ('nil', 'nil', 7, 'nil', 2, 'nil', 3, 9, 'nil'),
    ('nil', 'nil', 4, 1, 'nil', 9, 'nil', 'nil', 5)
)

csp = create_sudoku_csp(sudoku_board)
print("Variables and their domains:", csp['variables'])
print("Constraints (example subset):", csp['constraints'][:10])  # Displaying only the first few constraints for brevity
