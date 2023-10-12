import numpy as np


class Sudoku:
    
    def __init__(self, NestedList = []):
        
        # Redefines self as 'g', this is done in every function to speed up the coding process.
        g = self
        
        g.VisitedCells = [] # Stores all cells that have been visited by the search
        g.AvailableDigits = {} # Availale digits for each cell
        g.EmptyCells = set() # All empty cells that will need to be searched
        g.CompareEmptyCells = set() # Compares empty cells to see if they have been iterated
        g.Cell =  None # Will be used when iterating later in the programme
        g.NextCell = 0 # Will be used when iterating later in the programme
        g.SudokuCopy = [] # Keeps a copy of sudoku that is being solved
        g.Grid = [] # The grid that will be solved
        for x in NestedList: # Copies values of nested lists
            g.SudokuCopy.append(x[:])
            g.Grid.append(x[:])
        
    def ChooseCell(Grid, cell, value):
        # Function that chooses cell and sets it
        row = cell // 9
        column = cell % 9
        Grid[row][column] = value
        
    
    def PossibleDigits(Grid, cell):
        # Function that returns all possible digits for a cell within the rules of the sudoku through constraint propagation
        digits = {1,2,3,4,5,6,7,8,9}
        row = cell // 9
        column = cell % 9
        
        # Propagate chosen cell by removing the corresponding values in same row
        for j in range(0,9):
            if Grid[row][j] in digits:
                digits.remove(Grid[row][j])
                
        # Propagate chosen cell by removing the corresponding values in same column
        for i in range(0,9):
            if Grid[i][column] in digits:
                digits.remove(Grid[i][column])
                
        # Propagate chosen cell by removing the corresponding values in same 3x3 section
        # This is achieved by finding the floored quotient of the cell, multiplying it by three for the lower part of the range
        # and doing the same for the higher part of the range, however adding three to it as well
        for i in range((row//3)*3, (row//3)*3+3):
            for j in range((column//3)*3, (column//3)*3+3):
                if Grid[i][j] in digits:
                    digits.remove(Grid[i][j])
                    
        if len(digits) == 0: 
            return set() 
        else: 
            return set(digits)
        
    def CheckSudoku(Grid):
        # Function that checks if the sudoku has been completed
        
        # Check if all rows have been filled
        for i in range(9):
            counter = {0:1, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for j in range(9):
                counter[Grid[i][j]] += 1
            for x in counter:
                if counter[x] != 1:
                    return False
        
        # Check if all columns have been filled
        for i in range(9):
            counter = {0:1, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for j in range(9):
                counter[Grid[j][i]] += 1
            for x in counter:
                if counter[x] != 1:
                    return False
                
                
        # Check if all 3x3 sections have been filled
        def CheckSection(inputGrid, LowRow, HighRow, LowColumn, HighColumn):
            counter = {0:1, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for i in range(LowRow,HighRow + 1):
                for j in range(LowColumn, HighColumn + 1):
                    counter[inputGrid[i][j]] += 1
            for x in counter:
                if counter[x] != 1:
                    return False
            return True
        
        for i in range(0,7,3):
            for j in range(0,7,3):
                if not CheckSection(Grid, i, i+2, j, j+2):
                    return False
        return True
    
    def ReturnNextCell(EmptyCells):
        # Function that returns the next cell that is going to be iterated
        
        NextCellChoice = {}
        for id in EmptyCells:
            NextCellChoice[id] = 0
            
        return min(NextCellChoice, key = NextCellChoice.get)
    
    def NextDigit(Grid, AvailableDigits, Cell, ChooseCell):
        # Function that chooses next digit to set cell to
        NextCellDigit = {}
        for x in AvailableDigits[Cell]:
            NextCellDigit[x] = 0
            
        NextCell = min(NextCellDigit, key = NextCellDigit.get)
        ChooseCell(Grid, Cell, NextCell)
        AvailableDigits[Cell].remove(NextCell)
        
    
def sudoku_solver(self):
    # Function that solves the sudoku
    g = Sudoku
    
    # Resets all values before grid is solved
    g.Grid = self 
    g.SudokuCopy = []
    for x in g.SudokuCopy: 
        g.Grid.append(x[:])        

    g.VisitedCells = [] 
    g.AvailableDigits = {} 
    g.EmptyCells = set() 
    g.CompareEmptyCells = set() 
    g.Cell =  None 
    g.NextCell = 0 


    # Set which cells are empty and saves a copy for comparison
    for i in range(0,9):
        for j in range(0,9):
            if g.Grid[i][j] == 0:
                g.EmptyCells.add(9*i+j)
    g.CompareEmptyCells = set(g.EmptyCells)

    # Choose a first cell for the iterations
    g.Cell = g.ReturnNextCell(g.EmptyCells)
    g.AvailableDigits[g.Cell] = g.PossibleDigits(g.Grid, g.Cell)

    
    # Begin iterating the sudoku
    loop1 = 1
    while loop1 == 1:
        
        # If all cells are filled then call function to check the sudoku
        if len(g.EmptyCells) < 1:
            if g.CheckSudoku(g.Grid):
                #for x in range(9):
                 #    print(g.Grid[x])
                solved_sudoku = g.Grid
                print(solved_sudoku)
                return solved_sudoku
            
        # If there is an empty cell in the sudoku, move to the next cell
        if len(g.EmptyCells) > 0:
            # Return the next cell
            g.Cell = g.ReturnNextCell(g.EmptyCells)
            
            # Add the chosen cell to the visited cells list
            g.VisitedCells.append(g.Cell)
            
            # Remove the chosen cell from the stored empty cells
            g.EmptyCells.remove(g.Cell)
            
            # Get the possible digits for the chosen cell
            g.AvailableDigits[g.Cell] = g.PossibleDigits(g.Grid, g.Cell) 
            
            # If there is one or more available digits for the cell, select that digit and continue iterating
            if len(g.AvailableDigits[g.Cell]) > 0:
                g.NextDigit(g.Grid, g.AvailableDigits, g.Cell, g.ChooseCell)
                continue
        
        # Start backtracking process
        # Remove the cell from the visited cells list
        g.VisitedCells.remove(g.Cell)
        
        # Add the cell back to the stored empty cells
        g.EmptyCells.add(g.Cell)
        
        # Delete all of the digits for that cell and set it to 0
        del g.AvailableDigits[g.Cell]
        g.NextCell = 0
        g.ChooseCell(g.Grid, g.Cell, g.NextCell)
        
        # Backtrack to the previous cell
        while True:
            
            # If the number of visited cells is 0 then backtracking cannot continue and the sudoku cannot be solved
            if len(g.VisitedCells) < 1:
                solved_sudoku = FalseGrid
                print(solved_sudoku)
                return solved_sudoku
            
            # Set the current cell to the previous cell
            g.Cell = g.VisitedCells[-1]
            
            # Keep backtracking until a cell with available digits is found
            if len(g.AvailableDigits[g.Cell]) < 1:
                # Remove cell from the visited cells list
                g.VisitedCells.remove(g.Cell)
                
                # Add the cell back to the stored empty cells
                g.EmptyCells.add(g.Cell)
                
                # Delete all of the digits for that cell and set it to 0
                del g.AvailableDigits[g.Cell]
                g.NextCell = 0
                g.ChooseCell(g.Grid, g.Cell, g.NextCell)
                continue
            
            # When a cell with available digits is found, continue iterations of it and exit out of the backtrack iterations
            g.NextDigit(g.Grid, g.AvailableDigits, g.Cell, g.ChooseCell)
            break
        
FalseGrid =[[-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1,]]

abc = np.load(r'/Users/gustavdurlind1/Downloads/sudoku/data/hard_puzzle.npy')
for j in range(0,15):
    sudoku = abc[j]

    sudoku_solver(sudoku)

                   
