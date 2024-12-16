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
LEFT_RIGHT = {'U': ('L','R'), 'D': ('R','L'), 'L': ('D','U'), 'R': ('U','D')}

        
def bfs(start, end):
    q = [start[0],start[1]]
    heapq.heapify(q)
    visited = {}
    best = 0
    
    while q:
        dist, (i,j), d= heapq.heappop(q)
        if end == (i,j) and best==0:
            best = dist
        if (i,j,d) in visited.keys():
            continue
        visited[(i,j,d)] = dist
        ni, nj = i+DIR[d][0], j+DIR[d][1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != '#':
            heapq.heappush(q, (dist+1, (ni,nj), d))
        for new_d in LEFT_RIGHT[d]:
            heapq.heappush(q, (dist+1000, (i,j), new_d))
    return best, visited

p1,vs = bfs([(1000, start, 'U'), (0, start, 'R')], end)

#Go backwards
DIR = {'U': (1,0), 'D': (-1,0), 'L': (0,1), 'R': (0,-1)}
_,ve = bfs([(0, end, 'U'), (0, end, 'R')], start)

shortestPaths = set()
for i in range(R):
    for j in range(C):
        for d in DIR.keys():
            if (i,j,d) in vs and (i,j,d) in ve and vs[(i,j,d)] + ve[(i,j,d)] == p1:
                shortestPaths.add((i,j))
                
print(f'Part 1: {p1}')
print(f'Part 2: {len(shortestPaths)}')

'''
Variante 2 mit Dijkstra

def bfs2(start, end):
    q = [(0, start, 'R')]
    heapq.heapify(q)
    visited = {}
    pre = {}
    
    while q:
        dist, (i,j), d = heapq.heappop(q)
        for (nx,ny,nd,da) in [(i+DIR[d][0], j+DIR[d][1], d, dist+1), (i, j, LEFT_RIGHT[d][0], dist+1000), (i, j, LEFT_RIGHT[d][1], dist+1000)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                if (nx,ny,nd) not in visited:
                    visited[(nx,ny,nd)] = da
                    pre[(nx,ny,nd)] = [(i,j,d)]
                    heapq.heappush(q, (da, (nx,ny), nd))
                elif visited[(nx,ny,nd)] >= da:
                    pre[(nx,ny,nd)].append((i,j,d))
    return pre,min(visited[(end[0],end[1],'U')],visited[(end[0],end[1],'R')])

path,p1 = bfs2(start, end)
paths = set()
stack = {((end), 'R'), ((end), 'U')}
while stack:
    (i,j),d = stack.pop()
    if (i,j) == start:
        paths.add((i,j))
        continue
    for item in path[(i,j,d)]:
        ni,nj,nd = item
        paths.add((i,j))
        stack.add(((ni,nj),nd))
print(f'Part 1: {p1}')
print(f'Part 2: {len(paths)}')
'''