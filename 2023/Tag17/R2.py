from sys import argv
import math
with open(argv[1]) as f:
    content=f.read().splitlines()

grid = [[int(c) for c in line] for line in content]
R = len(grid)
C = len(grid[0])

def bfs(grid, start):
    x,y = start
    q = [(0, x, y, ((0,0),0))]
    visited = {}
    while q:
        d,x,y,dir = q.pop(q.index(min(q, key=lambda x: x[0])))
        if x == R-1 and y == C-1 and dir[1]>=3:
            return d
        if (x,y,dir) in visited:
            continue
        visited[(x,y,dir)] = d
        for dr,dc in ((0,1),(1,0),(0,-1),(-1,0)):
            if ((dr,dc) == dir[0] and dir[1] >= 9) or (dr,dc) == (-dir[0][0],-dir[0][1]) or ((dr,dc) != dir[0] and dir[0]!=(0,0) and dir[1]<3):
                continue
            
            nr,nc = x+dr,y+dc
            ndir = ((dr,dc), 0 if (dr,dc) != dir[0] else dir[1]+1)
            if 0 <= nr < R and 0 <= nc < C and (nr,nc,ndir) not in visited:
                q.append((d+grid[nr][nc],nr,nc,ndir))
        
print(bfs(grid, (0,0)))