with open('in.txt') as f:
    content = f.read().splitlines()
    
R = 71
C = 71
    
def bfs(start,end):
    q = [(start,0)]
    visited = set()
    
    while q:
        (i,j),d = q.pop(0)
        if (i,j) == end:
            return d
        if (i,j) in visited:
            continue
        visited.add((i,j))
        for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<=ni<R and 0<=nj<C and (ni,nj) not in walls:
                q.append(((ni,nj),d+1))

walls = set()
for k,line in enumerate(content):
    if k==1024:
        print(f'Part 1: {bfs((0,0),(R-1,C-1))}')
    j,i = [int(x) for x in line.split(',')]
    walls.add((i,j))
    if bfs((0,0),(R-1,C-1)) == None:
        print(f'Part 2: {j},{i}')
        break