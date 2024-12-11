from sys import argv
with open(argv[1]) as f:
    content = f.read().splitlines()

print(len("#...#.#.#.#...#...#...#.#...#...#...#...#.#.#.#.#.#.#...#.#.#...#...#...#.....#...#...#.#.###.#...#.#.#.#.#.....#.#.#...#.#.>."))
print(content[137][125])
    
def bfs(grid, start,end):
    q=[(start,0,(start))]
    paths = []
    while q:
        (x,y),d,visited = q.pop(0)
        if (x,y) == end:
            print(len(visited))
            paths.append(visited)
            continue
        if (137,125) in visited and (x,y) != (137,125):
            continue
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy] != '#' and (x+dx,y+dy) not in visited:
                q.append(((x+dx,y+dy),d+1,visited+((x+dx,y+dy),)))

    return len(paths[-1])-2

start = (0,content[0].index('.'))
end = (len(content)-1,content[-1].index('.'))

print(bfs(content,start,end))