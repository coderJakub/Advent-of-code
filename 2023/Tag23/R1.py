from sys import argv
with open(argv[1]) as f:
    content = f.read().splitlines()


    
def bfs(grid, start,end):
    q=[(start,0,(start))]
    paths = []
    direc = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}
    while q:
        (x,y),d,visited = q.pop(0)
        if (x,y) == end:
            paths.append(visited)
            continue
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy] != '#' and (x+dx,y+dy) not in visited and (grid[x][y] == '.' or (dx,dy) == direc[grid[x][y]]):
                q.append(((x+dx,y+dy),d+1,visited+((x+dx,y+dy),)))

    return len(paths[-1])-2

start = (0,content[0].index('.'))
end = (len(content)-1,content[-1].index('.'))

print(bfs(content,start,end))