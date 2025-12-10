from itertools import combinations
import sys

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = [list(map(int,line.split(','))) for line in f.read().splitlines()]
    
p1 = 0
for (x1, y1), (x2,y2) in combinations(content, 2): 
    p1 = max(p1, (abs(x1-x2)+1) * (abs(y1-y2)+1))
    
p2 = 0
polygon = {}

edgesH = []
edgesV = []
for (x1, y1), (x2, y2) in zip(content, content[1:] + content[:1]):
    if y1 == y2:
        edgesH.append((y1, sorted((x1,x2))))
    else:
        edgesV.append((x1, sorted((y1,y2))))
    

minY = min(e[1] for e in content)
maxY = max(e[1] for e in content)

for yScan in range(minY, maxY + 1):
    xs = sorted([x for x, (y1,y2) in edgesV if y1 <= yScan < y2])
    intervals = list(zip(xs[::2], xs[1::2]))
    intervals += [(x1, x2) for y, (x1, x2) in edgesH if yScan == y]
    
    intervals.sort()
    merged = []
    for a, b in intervals:
        if not merged or a > merged[-1][1]:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    polygon[yScan] = merged


for i, ((x1, y1), (x2,y2)) in enumerate(combinations(content, 2)):
    xs = sorted([x1,x2])
    ys = sorted([y1,y2])
    if all(
        any(a<=xs[0] and xs[1]<=b for (a,b) in polygon[y]) 
        for y in range(ys[0], ys[1]+1)
    ):
        p2 = max(p2, (xs[1]-xs[0]+1) * (ys[1]-ys[0]+1))


print(f'Part 1: {p1}')
print(f'Part 2: {p2}')