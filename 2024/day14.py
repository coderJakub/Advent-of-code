from collections import defaultdict
import time
with open('in.txt') as f:
    content = f.read().splitlines()

R=103
C=101
k=0

def bfs(start, endPos):
    q = [start]
    visited = set()
    visited.add(start)
    while q:
        x,y = q.pop(0)
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if (x+dx,y+dy) in endPos and (x+dx,y+dy) not in visited:
                visited.add((x+dx,y+dy))
                q.append((x+dx,y+dy))
    return visited

while True:
    k+=1
    endPos = defaultdict(int)
    for line in content:
        pos, v = line.split(' ')
        x,y = [int(x) for x in pos[2:].split(',')]
        xx,yy = [int(x) for x in v[2:].split(',')]
        x,y = (x+xx*k)%C, (y+yy*k)%R
        endPos[(x,y)] += 1
    
    if k==100:
        q = [0,0,0,0]
        for (x,y),v in endPos.items():
            if x<C//2 and y<R//2:
                q[0] += v
            elif x>C//2 and y>R//2:
                q[3] += v
            elif x<C//2 and y>R//2:
                q[2] += v
            elif x>C//2 and y<R//2:
                q[1] += v

        print(f'Part 1: {q[0]*q[1]*q[2]*q[3]}')
    
    seen=set()
    for (x,y) in list(endPos.keys()):
        if (x,y) in seen:
            continue
        visited = bfs((x,y),list(endPos.keys()))
        if len(visited)>30:
            print('Part 2:', k)
            exit()
        for v in visited:
            seen.add(v)