from typing import Dict, List, Tuple

Grid = List[List[int]] # type alias.
Flashed = List[Tuple[int, int]] # type alias for flashed list.

flashes = 0

def pretty_print(grid: Grid):
    for row in grid:
        print("".join(map(str, row)))
    print("")

def increase_fn(i: int, j: int, grid: Grid) -> Flashed:
    def increase() -> Flashed:
        if i < 0 or j < 0:
            raise Exception("out of bounds")
        
        grid[i][j] += 1
        if grid[i][j] == 10:
            global flashes
            flashes += 1
            return iluminate(i, j, grid)
    return increase

# iluminate is called when energy is greater than 9.
def iluminate(i: int, j: int, grid: Grid) -> Flashed:
    flashed = [(i, j)]

    increase_steps = [
        increase_fn(i-1, j, grid),
        increase_fn(i-1, j-1, grid),
        increase_fn(i-1, j+1, grid),
        increase_fn(i, j+1, grid),
        increase_fn(i, j-1, grid),
        increase_fn(i+1, j, grid),
        increase_fn(i+1, j-1, grid),
        increase_fn(i+1, j+1, grid),
    ]
    
    for step in increase_steps:
        try:
            flashed.extend(step()) # try to increase adjacent energy.
        except Exception as e:
            pass

    return flashed
        

def step(step: int, grid: Grid):
    flashed = []
    for i, row in enumerate(grid):
        for j, energy in enumerate(row):
            grid[i][j] += 1
            if energy + 1 == 10:
                global flashes
                flashes += 1
                flashed.extend(iluminate(i, j, grid))
    print(f"flashed: {flashed} for step {step}")
    for i, j in flashed:
        grid[i][j] = 0


def solve(grid: Grid):
    for i in range(100):
        step(i+1, grid)
    pretty_print(grid)
    print(f"flashes: {flashes}")

with open('11/input.txt') as f:
    grid = [[int(char) for char in line.replace('\n', '')] for line in f]
    solve(grid)
    