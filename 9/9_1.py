from typing import List, Tuple

def sum_lowest(points: Tuple, grid: List[List]) -> int:
    sum: int = 0
    for i, j in points:
        sum += int(grid[i][j]) + 1
    return sum

def check_if_lowest(i: int, j: int, grid: List[List]) -> bool:
    el: int = grid[i][j]
    try: 
        if i != 0:
            if el >= grid[i-1][j]:
                return False
        if j != 0:
            if el >= grid[i][j-1]:
                return False
        if i != len(grid)-1:
            if el >= grid[i+1][j]:
                return False
        if j != len(grid[0])-1:
            if el >= grid[i][j+1]:
                return False
            
    except Exception as e:
        return False
    return True


def solve():
    lowest = {}
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f]
        
        # loop through every element in the grid. 
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if check_if_lowest(i, j, grid):
                    lowest[(i,j)] = True

    print(sum_lowest(list(lowest.keys()), grid))

        
if __name__ == "__main__":
    solve()