from flask import Flask, render_template, request
from flask_cors import CORS
from utility.generatePuzzle import generate_csp
from utility.parse_string import parse_string
from backtrack import backtrack
from puzzles.sudoku_constraints9x9 import constraints9x9 as constraints
import math
import copy

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("input.html")


@app.route("/solve", methods=["POST"])
def solve():

    csp_input = request.form["puzzle"]
    puzzle = parse_string(csp_input)
    puzzle = generate_csp(puzzle)
    puzzle["constraints"] = copy.deepcopy(constraints)

    assignment, order, to_assign, failed, prev, steps = backtrack(puzzle)
    intermediate_steps = []  # stores info for each individual board state
    print(f"\n=====================Assignments=====================\n{assignment}")
    print(f"\n=====================Order=====================\n{order}")
    print(f"\n=====================To Assign=====================\n{to_assign}")
    print(f"\n=====================Failed=====================\n{failed}")
    print(f"\n=====================Prev=====================\n{prev}")

    for step in steps:
        state = step["state"]
        rows = []
        for i in range(
            int(math.sqrt(len(assignment)))
        ):  # dynamically adjust for different sizes of sudoku
            row = []
            for j in range(int(math.sqrt(len(assignment)))):
                cell_key = f"C{i+1}{j+1}"
                value = state.get(cell_key)
                guessed = cell_key in order
                failed_values = failed.get(cell_key, [])
                is_backtracked = step["step"] == "backtrack" and step["var"] == cell_key
                row.append(
                    {
                        "value": value,
                        "guessed": guessed,
                        "failed_values": failed_values,
                        "is_backtracked": is_backtracked,
                    }
                )
            rows.append(row)
        intermediate_steps.append(rows)

    return render_template("display.html", intermediate_steps=intermediate_steps)


if __name__ == "__main__":
    app.run(debug=True)
