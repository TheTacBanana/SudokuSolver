import copy, time, sys
sys.setrecursionlimit(10000)

def CheckValid(grid, numpos, num, checkfinish=False):
    newGrid = copy.deepcopy(grid)
    if not checkfinish: newGrid[numpos[0]][numpos[1]] = num

    validcols = [len(set(i)) == len(i)for i in [[newGrid[y][x] for x in range(9) if newGrid[y][x] != 0]for y in range(9)]]
    validrows = [len(set(i)) == len(i)for i in [[newGrid[x][y] for x in range(9) if newGrid[x][y] != 0]for y in range(9)]]
    boxes = [[newGrid[(3 * (out // 3)) + (inn // 3)][(3 * (out % 3)) + (inn % 3)]for inn in range(9)if newGrid[(3 * (out // 3)) + (inn // 3)][(3 * (out % 3)) +(inn % 3)] != 0] for out in range(9)]
    validboxes = [len(set(i)) == len(i) for i in boxes]

    if checkfinish and not False in [len(i) == 9 for i in boxes] and not False in validcols and not False in validrows and not False in validboxes: return True
    elif checkfinish or (False in validcols or False in validrows or False in validboxes): return False
    else: return True

def Search(grid, pos=0):
    if CheckValid(grid, None, None, True): return True, grid

    x = pos % 9
    y = pos // 9
    if grid[y][x] == 0:
        flag = False
        for i in range(1, 10):
            if CheckValid(grid, [y, x], i):
                flag = True
                newGrid = copy.deepcopy(grid)
                newGrid[y][x] = i
                result, returngrid = Search(newGrid)

                if result: return True, returngrid
                else: continue
        if not flag: return False, None
    else:
        newGrid = copy.deepcopy(grid)
        result, returngrid = Search(newGrid, copy.copy(pos) + 1)
        if result: return True, returngrid

    return False, None

def PrintGrid(grid):
    out = ""
    for y in range(9):
        temp = ""
        if (y) % 3 == 0 and y != 0: 
            temp += "".join(["#" if (i+2) % 8 == 0 else "-" for i in range(21)]) + "\n"
        for x in range(9):
            if grid[y][x] != 0: temp += str(grid[y][x]) + " "
            else: temp += "- "
            if (x + 1) % 3 == 0 and x != 8: temp += "| "
        out += temp + "\n"
    print(out)

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 2, 1, 9, 5, 0, 0, 0],
[1, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 1, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 2, 8, 0, 0, 7, 9]]

PrintGrid(grid)

starttime = time.time()
_, newgrid = Search(grid)

print(newgrid)
PrintGrid(newgrid)
print(f"Solve Time: {time.time() - starttime}")