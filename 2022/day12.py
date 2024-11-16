from sys import argv

with open(argv[1]) as f:
    grid = [list(line) for line in f.read().splitlines()]

def findStart(grid):
    start = []
    end = []
    for i,line in enumerate(grid):
        try:
            j = line.index('S')
            start = [i,j]
            grid[i][j] = 'a' 
        except:
            pass
        try:
            j = line.index('E')
            end = [i,j]
            grid[i][j] = 'z'
        except:
            pass
    return [start, end]
def bfs(grid, start, end = []):
    count = 0
    d = []
    d1 = [start]
    found = [start]
    while not d1 == []:
        d = d1
        d1 = []
        while not d == []:
            idx = d.pop(0)
            if end == [] and grid[idx[0]][idx[1]] == 'a':
                return count
            elif idx == end:
                return count
            for dir in [[0,1], [0,-1], [1,0], [-1,0]]:
                nextIdx = [idx[0]+dir[0], idx[1]+dir[1]]
                try:
                    if ord(grid[nextIdx[0]][nextIdx[1]]) >= ord(grid[idx[0]][idx[1]])-1:
                        if not nextIdx in d1 and not nextIdx in found:
                            d1.append(nextIdx)
                            found.append(nextIdx)
                except:
                    pass
        count +=1

start, end = findStart(grid)
print(f'Part 1: {bfs(grid, end, start)}') #starts searching from end to start
print(f'Part 2: {bfs(grid, end)}') #starts searching from end to first a