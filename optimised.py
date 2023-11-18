import time, copy
def CheckValid(grid):
    if False in [len(set([i for i in j if i != 0])) == len([i for i in j if i != 0]) for j in [grid[i:i+9] for i in range(0, 81, 9)]]: return False
    if False in [len(set([i for i in j if i != 0])) == len([i for i in j if i != 0]) for j in [[grid[i + k] for k in range(0, 81, 9)] for i in range(9)]]: return False
    if False in [len(set([i for i in j if i != 0])) == len([i for i in j if i != 0]) for j in [(grid[27*k+3*j:27*k+3*j+3] + grid[27*k+3*j+9:27*k+3*j+12] + grid[27*k+3*j+18:27*k+3*j+21]) for j in range(3) for k in range(3)]]: return False
    return True

def Search(grid, pos=0):
    if pos == 81:
        return grid
    elif grid[pos] == 0:
        #newgrid = copy.copy(grid)
        for i in {1,2,3,4,5,6,7,8,9}.difference(grid[9*(pos//9):9*(pos//9)+9]):
            grid[pos] = i
            if CheckValid(grid):
                result = Search(grid, pos + 1)
                if result: return result
        grid[pos] = 0
        return False
    else: 
        return Search(grid, pos + 1)

def PrintGrid(grid):
    out = ""
    for i in range(0, 81, 9):
        temp = ""
        cur = grid[i:i+9]
        for j in range(len(cur)):
            temp += f"{cur[j] if cur[j] != 0 else '-'} "
            if (j + 1) % 3 == 0 and j != 8:
                temp += "| "
        out += temp + "\n"
        if (i+9) % 27 == 0 and i != 72: out += "".join(["#" if (i+2) % 8 == 0 else "-" for i in range(21)]) + "\n"
    print(out)

grid = [0, 0, 0, 0, 8, 0, 0, 0, 7,
 0, 0, 0, 0, 0, 1, 0, 0, 8,
 0, 0, 0, 0, 2, 5, 1, 4, 0,
 0, 0, 0, 0, 0, 8, 0, 3, 0,
 3, 0, 4, 0, 0, 0, 0, 0, 6,
 0, 7, 2, 5, 0, 0, 4, 0, 0,
 0, 0, 1, 0, 0, 9, 0, 7, 0,
 0, 0, 7, 1, 0, 0, 5, 0, 0,
 6, 3, 0, 0, 5, 0, 0, 0, 0]


PrintGrid(grid)

start = time.time()

out = Search(grid)
end = time.time()

PrintGrid(out)
print(f"Solved In: {end - start}")