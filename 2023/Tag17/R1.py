from sys import argv
import math
with open(argv[1]) as f:
    content=f.read().splitlines()

grid = [[int(c) for c in line] for line in content]
R = len(grid)
C = len(grid[0])

def bfs(grid, end):
    queue = [[(0,0), 0, [[0,0],0]]]
    visited = set()
    
    while queue:
        pos, dist, dir = queue.pop(queue.index(min(queue, key=lambda x: x[1])))
        visited.add(pos)
        print(f'{len(visited)} von {R*C}')
        if pos == end:
            return dist
        
        for i, j in [[0,1],[1,0],[0,-1],[-1,0]]:
            x, y = pos[0]+i, pos[1]+j
            if 0<=x<R and 0<=y<C and (x,y) not in visited and (dir[0] != [i,j] or dir[1] < 3):
                queue.append([(x,y), dist+grid[x][y], [[i,j], 1 if dir[0] != [i,j] else dir[1]+1]])
    
print(bfs(grid, (R-1, C-1)))