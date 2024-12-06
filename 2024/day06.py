from copy import deepcopy
with open('in.txt') as f:
    content = [[c for c in line] for line in f.read().splitlines()]

R = len(content)
C = len(content[0])
    
for i, line in enumerate(content):
    if line.count('^')>0:
        start = (i, line.index('^'))
        
def findPathOut(grid,start):
    x,y = start
    d = [[-1,0],[0,1],[1,0],[0,-1]]
    di = 0
    visited = set()
    visited_with_direction = set()
    visited.add((x,y))
    visited_with_direction.add((x,y,di))
    iter = 0
    while 0<=x+d[di][0]<R and 0<=y+d[di][1]<C:
        if (x+d[di][0],y+d[di][1],di) in visited_with_direction:
            return None
        if grid[x+d[di][0]][y+d[di][1]] == '#':
            di = (di+1)%4
            continue
        x,y = x+d[di][0],y+d[di][1]
        visited.add((x,y))
        visited_with_direction.add((x,y,di))
        iter += 1
    return len(visited)

print(f'Part 1: {findPathOut(content,start)}')

count =0
for i,line in enumerate(content):
    for j,c in enumerate(line):
        if c == '#' or c == '^':
            continue
        newContent = deepcopy(content)
        newContent[i][j] = '#'
        if findPathOut(newContent,start) is None:
            count += 1

print(f'Part 2: {count}')