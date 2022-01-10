from typing import List
import math

# find_basin takes current location and copy of grid and starts traveling towards the lowest point.
def find_basin(i: int, j: int, grid: List[List], first: str) -> int:
    if grid[i][j] == "#": # we were here
        return 0


    el = grid[i][j]
    if el == '9':
        return 1
    grid[i][j] = "#"

    sum = 1

    if i != 0:
        if grid[i-1][j] <= first:
            sum +=  find_basin(i-1, j, grid, first) 
    if j != 0:
        if  grid[i][j-1] <= first:
            sum +=  find_basin(i, j-1, grid, first) 
    if i != len(grid)-1:
        if  grid[i+1][j] <= first:
            sum += find_basin(i+1, j, grid, first)
    if j != len(grid[0])-1:
        if  grid[i][j+1] <= first:
            sum += find_basin(i, j+1, grid, first)
    return sum

def solve():
    values = []
    with open("9/input.txt") as f:
        grid = [list(line.strip()) for line in f]
        
        # loop through every element in the grid. 
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                size = find_basin(i, j, grid, grid[i][j])
                values.append(size)
    values.sort(reverse=True)
    print(math.prod(values[:3]))

        
if __name__ == "__main__":
    solve()