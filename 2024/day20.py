from collections import defaultdict
with open('in.txt') as file:
    content = file.read().splitlines()
    

def bfs(start):
    q = [(start,0)]
    visited = {}
    
    while q:
        (i,j),d = q.pop(0)
        if (i,j) in visited:
            continue
        else:
            visited[(i,j)] = d
        
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0<=i+dx<R and 0<=j+dy<C and content[i+dx][j+dy] != '#':
                q.append(((i+dx,j+dy),d+1))
    return visited

def checkCheat(start,visited, abbr):
    si,sj = start
    q = [((si,sj),0)]
    seen = set()
    while q:
        (i,j),d = q.pop(0)
        if d > abbr or (i,j) in seen:
            continue
        seen.add((i,j))
        if content[i][j] != '#' and (i,j)!=start:
            pointPairs[((si,sj),(i,j))] = max(pointPairs[((si,sj),(i,j))],visited[(si,sj)]-visited[(i,j)]-d)
            continue
                
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0<=i+dx<R and 0<=j+dy<C:
                q.append(((i+dx,j+dy),d+1))
    
R = len(content)
C = len(content[0])

for i in range(R):
    for j in range(C):
        if content[i][j] == 'E':
            visited = bfs((i,j))
            break

for p,time in [('1',2),('2',20)]:
    pointPairs = defaultdict(int)
    count= 0
    for i in range(R):
        for j in range(C):
            if content[i][j] != '#':
                checkCheat((i,j),visited,time)
    for k,v in pointPairs.items():
        if v>=100:
            count+=1
    print(f'Part {p}: {count}')