# Sudoku solver
# Wessel Martens
# 1-Jan-2020

def zeroIndex(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def checkRow(grid, row, col, digit):
    for idx in range(9):
        if idx != col and grid[row][idx] == digit:
            return False
    return True

def checkCol(grid, row, col, digit):
    for idx in range(9):
        if idx != row and grid[idx][col] == digit:
            return False
    return True

def checkBox(grid, row, col, digit):
    for boxrow in range(3):
        for boxcol in range(3):
            if boxrow != row%3 and boxcol != col%3 and grid[row-row%3+boxrow][col-col%3+boxcol] == digit:
                return False
    return True

def checkValid(grid, row, col, digit):
    return checkRow(grid, row, col, digit) and checkCol(grid, row, col, digit) and checkBox(grid, row, col, digit)

def displayGrid(grid):
    for idx in range(9):
        print(grid[idx])

def solveSudoku(grid):
    row, col = zeroIndex(grid)
    if row != None and col != None:
        for digit in range(1,10):
            if checkValid(grid, row, col, digit):
                grid[row][col] = digit
                if solveSudoku(grid):
                    return True
                else:
                    grid[row][col] = 0
        return False
    else:
        displayGrid(grid)
        return True

# If you run your Python file directly, Python will assign to variable __name__ the string '__main__'
# then evaluating the condition below will result in a direct execution of the .py file
# note: by default, the Python interpreter will evaluate this statement if it's not there
# If you import modules, the statement allows you to control the execution of the modules
if __name__ == '__main__':
    puzzle = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    solveSudoku(puzzle)