import time, copy
def CheckValid(grid):
    if False in [len(set(removezero:=[r for r in row if r != 0])) == len(removezero) for row in grid]: return False

    for i in range(9):
        list = []
        for row in grid:
            list.append(row[i])

        removezero = [i for i in list if i != 0]
        if len(set(removezero)) != len(removezero):
            return False

    for i in range(3):
        for j in range(3):
            tile = []
            for down in range(3):
                tile.extend(grid[j * 3 + down][i * 3:i * 3 + 3])
            removezero = [t for t in tile if t != 0]
            if len(set(removezero)) != len(removezero):
                return False
    return True

def Search(grid, pos=0):
    div = pos//9
    mod = pos%9
    if pos == 81:
        return True, grid
    elif grid[div][mod] == 0:
        for i in {1,2,3,4,5,6,7,8,9}.difference(grid[div]):
            grid[div][mod] = i
            if CheckValid(grid):
                result, returngrid = Search(grid, pos + 1)
                if result: return result, returngrid
        grid[div][mod] = 0
        return False, None
    else: 
        return Search(grid, pos + 1)

grid = [[0, 0, 0, 0, 8, 0, 0, 0, 7],
 [0, 0, 0, 0, 0, 1, 0, 0, 8],
 [0, 0, 0, 0, 2, 5, 1, 4, 0],
 [0, 0, 0, 0, 0, 8, 0, 3, 0],
 [3, 0, 4, 0, 0, 0, 0, 0, 6],
 [0, 7, 2, 5, 0, 0, 4, 0, 0],
 [0, 0, 1, 0, 0, 9, 0, 7, 0],
 [0, 0, 7, 1, 0, 0, 5, 0, 0],
 [6, 3, 0, 0, 5, 0, 0, 0, 0]]
    
'''
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 2, 1, 9, 5, 0, 0, 0],
        [1, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 1, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 2, 8, 0, 0, 7, 9]]'''

for i in grid:
    print(i)

start = time.time()

result, out = Search(grid)
end = time.time()

print()
for i in out:
    print(i)

print(f"Solved In: {end - start}")