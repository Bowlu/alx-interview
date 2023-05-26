#!/usr/bin/python3

""" function that returns the perimeter
of the island"""

def island_perimeter(grid):
  perimeter = 0
  if type(grid) != list:
    return 0
  row = len(grid)
  column = len(grid[0])
  
  for r in range(row):
    for c in range(column):
      if grid[r][c] == 1:
        perimeter += 4
        if r > 0 and grid[r-1][c] == 1:
          perimeter -= 2
        if c > 0 and grid[r][c-1] == 1:
          perimeter -= 2
  return perimeter