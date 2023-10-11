# SudokuAI
Sudoku Solving AI Agent

My solution to the ‘Solving Sudoku Puzzles’ CM20252 assignment is made up of 7 functions, using constraint propagation, backtracking and depth-first search to solve each sudoku of varying difficulty. 

I started by defining all the necessary variables, lists and dictionaries in the ‘__init__’ function. 

These include a list that store each cell that has been visited by the search and a dictionary of available digits for each cell, as well as storing all empty cells which will need to be searched. 

The next function (‘ChooseCell’) chooses and sets the cell which will be searched, this is called later on in the programme. 

The ‘PossibleDigits’ function uses constraint propagation to remove the rows, columns and 3x3 sections of each searched cell, therefore eliminating the number of cells to search in the next iteration. 

I then added a ‘CheckSudoku’ function which goes through the entire sudoku and checks that each cell has been filled with a digit, this is called later in the programme when checking to see if the sudoku has been solved. 
