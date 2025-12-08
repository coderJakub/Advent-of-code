import sys
import math
import heapq

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = [list(map(int,line.split(','))) for line in f.read().splitlines()]
    
circuits = [{k} for k in range(len(content))]
distances = []
p1 = 1
p2 = 0

for i, (x1,y1,z1) in enumerate(content):
    for j, (x2,y2,z2) in enumerate(content[i+1:], start=i+1):
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        distances.append((d,i,j))

for l, [d,a,b] in enumerate(sorted(distances)):
    if l==1000: 
        p1 = math.prod(len(s) for s in heapq.nlargest(3, circuits, key=len))
    
    groupA = groupB = None
    for k, c in enumerate(circuits):
        if a in c: groupA = k
        if b in c: groupB = k
        if groupA is not None and groupB is not None: break
    
    if groupA!=groupB:
        circuits[groupA] |= circuits[groupB]
        circuits.pop(groupB)
    
    if len(circuits[0])==len(content):
        p2 = (content[a][0]*content[b][0])
        break

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')