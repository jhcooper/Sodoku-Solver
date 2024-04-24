# Sudoku Solver Using Backtracking with MRV Heuristic and AC3

Provides a web interface for solving Sudoku puzzles using backtracking with the Minimum Remaining Values (MRV) heuristic and the Arc Consistency 3 (AC3) algorithm.


## Project Setup Instructions

To get started with the Sudoku Solver web app, follow the following environment setup steps

1. **Prerequisites**
   
Ensure you have [Python](https://www.python.org/downloads/).
installed on your machine. This project has been tested with Python 3.9+ and above.

2. **Cloning the Repository**

Open terminal and use the following command to clone this repository to your local machine

```bash
git clone https://github.com/jhcooper/Sudoku-Solver.git
```

3. **Navigate to the Project Directory**
```bash
cd Sudoku-Solver
```

4. **Start a Virtual Environment**
   
This isn't required but helps with managing dependencies
```bash
python -m venv sudoku-env
```

5. **Activate the Virtual Environment**

For Windows:
```bash
sudoku-env\Scripts\activate
```

For MacOS and Linux:
```bash
source sudoku-env/bin/activate
```

6. **Install the Required Dependencies**
   
```bash
pip install -r requirements.txt
```

7. **Run the Application**

```bash
python flaskr/app.py
```

8. **Open the Application in your Browser**
Navigate to the URL displayed when app.py is ran for instance `http://127.0.0.1:5000/` from 
```bask 
(Sudoku-env) (base) jh@Johns-MacBook-Pro-2 Sudoku-Solver % python flaskr/app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 105-850-459
```



## Project Structure

All project-related files and ode can be found within the `flaskr` directory. 

`project2` contains configuration files for a virtual environment and the dependencies required for the project.


### Flaskr Directory

The `flaskr` directory contains the following folders and files:

- **Puzzles (Folder)**: A folder containing various CSP representations of some of the puzzles found in the directions, as well as the original `sudoku-constraints.lisp` file

- **Templates (Folder)**: Contains the HTML files for the web interface
  - `input.html` to handle user input 
  - `display.html` to display the solved puzzle steps.

- **Unused (Folder)**:
  - the original `sudoku-constraints.lisp` 
  - a python script I wrote to convert it to a python dictionary (`'generate-python-constraints.py`), and the output of that program

- **Utility (Folder)**: Contains 
  - `parse_string.py` which is used to parse the input string from the user into a 2d list of *int* and *None* values
  - `generatePuzzle.py`

- `part1.py`: Contains the CSP representation of Figure 4
- `ac3.py`: Contains the AC3 algorithm implementation
- `backtracking.py`: Contains the backtracking algorithm implementation
- `mrv.py`: Contains the MRV heuristic implementation
- `revise.py`: Contains the revise function used in the AC3 algorithm
- `app.py`: Contains the Flask application code


## Project Notes

- Backtrack returns a steps list in addition to the requirements that contains information for reproducing each step of the sudoku solution.

- In the final display, failed values (ones that led to backtrack) are displayed as smaller red numbers, (couldn't figure out the color changing on backtrack)

- It will finish running if the puzzle is solvable, just might take a while



## Input Format
The input format is basically a lisp alist without the `defvar` , so as an example, the input for the first puzzle would be:

```python
((nil nil nil nil nil 6 nil 8 nil)
(3 nil nil nil nil 2 7 nil nil)
(7 nil 5 1 nil nil 6 nil nil)
(nil nil 9 4 nil nil nil nil nil)
(nil 8 nil nil 9 nil nil 2 nil)
(nil nil nil nil nil 8 3 nil nil)
(nil nil 4 nil nil 7 8 nil 5)
(nil nil 2 8 nil nil nil nil 6)
(nil 5 nil 9 nil nil nil nil nil))
```
It should also work all on one line