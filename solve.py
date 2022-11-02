import math

# Example grid
grid = [
   [0,0,6, 0,4,0, 0,9,7],
   [0,4,0, 7,3,0, 0,1,0],
   [0,1,7, 0,9,2, 0,3,0],

   [6,0,0, 0,7,0, 0,8,0],
   [1,0,5, 0,6,0, 9,0,3],
   [0,2,0, 0,1,0, 0,0,6],

   [0,5,0, 9,8,0, 1,6,0],
   [0,9,0, 0,5,6, 0,7,0],
   [8,6,0, 0,2,0, 3,0,0],
]

# Check whether the number is already in the current row
def inRow(num, row):
    return num in grid[row]

# Check whether the number is already in the current column
def inColumn(num, column):
    for item in range(9):
        if grid[item][column] == num:
            return True
    return False

def inSquare(num, row, column):
    # Get correct square
    startRow = 3 * math.floor(row / 3)
    startCol = 3 * math.floor(column / 3)

    # Check every value in square
    for i in range(startRow, startRow + 3):
        for j in range (startCol, startCol + 3):
            if grid[i][j] == num:
                return True
    return False

# Check whether a number is possible
def possible(num, row, column):
    return not(inRow(num, row) or inColumn(num, column) or inSquare(num, row, column))


# code to actually solve the puzzle
def solve():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if possible(num, i, j):
                        grid[i][j] = num
                        solve()
                        grid[i][j] = 0
                return
    for item in grid:
        print(item)
    
    exit()
    
    

solve()