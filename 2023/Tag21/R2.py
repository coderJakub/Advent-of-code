from sys import argv
import pyperclip as pc
fn = argv[1] if len(argv) > 1 else 'input.txt'
with open(fn) as f:
    content = f.read().splitlines()

def printc(text):
    print(text)
    pc.copy(text)
    
new = []
for _ in range(5):
    for i,line in enumerate(content):
        fstr =''
        for _ in range(5):
            for c in content[i]:
                fstr += c if c!='S' else '.'
        new.append(fstr)
            
R = len(new)
C = len(new[0])

RC = len(content)
CC = len(content[0])

def bfs(start,grid):
    q = [(start,0)]
    distance = {}
    while q:
        (i,j),d = q.pop(0)
        if (i,j) in distance.keys():
            continue
        distance[(i,j)] = d
        for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#':
                q.append(((ni,nj),d+1))
    return distance

for i,l in enumerate(content):
    for j,c in enumerate(l):
        if c == 'S':
            distance_to_each = bfs((i+2*RC,j+2*CC),new)
            break
p1 = 0
for ii in range(RC):
    for jj in range(CC):
        i = ii+2*RC
        j = jj+2*CC
        if (i,j) not in distance_to_each:
            continue
        dist_pos =distance_to_each[(i-RC,j)] - distance_to_each[(i,j)]
        dist_neg =distance_to_each[(i+RC,j)] - distance_to_each[(i,j)]
        if i < RC//2:
            dist = dist_pos
            dist1 = distance_to_each[(i-RC,j)]
            dist2 = distance_to_each[(i-2*RC,j)]
        else:
            dist = dist_neg
            dist1 = distance_to_each[(i+RC,j)]
            dist2 = distance_to_each[(i+2*RC,j)]
        #assert dist1+dist == dist2, p1
        if dist1+dist == dist2:
            p1 +=1
        else:
            print(dist1,dist,dist2)
print(p1,RC*CC)  