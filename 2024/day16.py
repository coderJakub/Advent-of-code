import heapq

with open('in.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]

R = len(grid)
C = len(grid[0])

for i,line in enumerate(grid):
    for j,c in enumerate(line):
        if c == 'S':
            start = (i,j)
            grid[i][j] = '.'
        if c == 'E':
            end = (i,j)
            grid[i][j] = '.'

DIR = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}

def bfs(start, end):
    q = [(0, start, '',[start])]
    heapq.heapify(q)
    visited = {}
    while q:
        dist, (i,j), d, p = heapq.heappop(q)
        if end == (i,j):
            return dist
        if (i,j) in visited.keys():
            continue
        visited[(i,j)] = dist
        for k,v in DIR.items():
            ni, nj = i+v[0], j+v[1]
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != '#':
                heapq.heappush(q, (dist+(1 if d==k else 1001), (ni,nj), k, p+[(ni,nj)]))
                    
p1 = bfs(start, end)
print(p1)