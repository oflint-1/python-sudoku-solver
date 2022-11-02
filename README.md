---
layout: "../../layouts/BlogPost.astro"
title: "How to Solve Sudoku with Python"
description: ""
pubDate: "Oct 12 2022"
heroImage: "/sudoku.jpg"
heroCredit: "Photo by John Morgan on Unsplash"
---

Sudoku puzzles can range from criminally easy to extermely difficult. With python however, we can solve (most) sudoku puzzles within seconds. In this article, we'll develop an algorithm to solve a sudoku puzzle.

## Representation
For this problem we'll need two main components. Firstly, a way to represent our crossword puzzle. Ideally, we'll need a data structure with a quick access and modification time. We'll use a 2d array for this project. Lets get this setup in python:

```python
grid = [
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],

    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],
]
```
This will initialise our empty grid, with zeros in every square. Thats our representation pretty much sorted, so we can move onto actually solving a given crossword puzzle.

## Utility functions
We're going to create some utility functions which will greatly help our solution down the line. Each of these will perform checks for the standard rules of sudoku. 

Lets start by checking whether a number is in a given row. This is very simple, as we have each row stored within our grid array.

```python
def inRow(num, row):
    return num in grid[row]
```

Now, we can check columns. This will be slighlty more tricky, but still fairly straightforward. We just need to check the same column in each row, and return `True` if we find it.

```python
def inColumn(num, column):
    for item in range(9):
        if grid[item][column] == num:
            return True
    return False
```

Finally, we need to check whether a number exists already within a given square. We first calculate the square to check, and then check all locations within that square. Add `import math` to the top of you python file, and add the below function.

```python
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
```

Now these are done, we need a function to determine whether we can place a number in a certain position. We will create a `possible` function to do this. 
```python
def possible(num, row, column):
    return not(inRow(num, row) or inColumn(num, column) or inSquare(num, row, column))
```
We check to see whether the number is already in the given row or column, and return True if it is not present.

With these three utility functions, it is fairly straightforward to solve the sudoku.

## Solving the puzzle

We will now create our recursive solve function to complete the sudoku. We iterate through each square in the grid, checking whether we can place any number between 1 and 9 in the location. If there are no possible numbers to place in this location, we backtrack and try a different number.

```python
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
```

When we have found a solution, we output the solution and exit the program. Without this, the program would find all possible solutions, which could take some time...

With that, our program is complete! We have successfully written a program to solve any sudoku puzzle. Feel free to expand this algorithm, and built a fleshed out Sudoku Solver.
