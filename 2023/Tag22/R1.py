from sys import argv
from collections import defaultdict

with open(argv[1]) as f:
    content = f.read().splitlines()
    
done = []
support = defaultdict(list)

def intersect(a,b):
    return max(a[0],b[0]) <= min(a[1],b[1])

blocks = []
for line in content:
    xs,ys,zs = [int (x) for x in line.split("~")[0].split(",")]
    xe,ye,ze = [int (x) for x in line.split("~")[1].split(",")]
    blocks.append(((xs,ys,zs),(xe,ye,ze)))
blocks.sort(key=lambda x: x[0][2])
for k,line in enumerate(blocks):
    xs,ys,zs = line[0]
    xe,ye,ze = line[1]
    while min(zs,ze) > 1:
        canFall = True
        for i,block in enumerate(done):
            if max(block[0][2],block[1][2])+1 == min(zs,ze) and (intersect((block[0][0],block[1][0]),(xs,xe)) and intersect((block[0][1],block[1][1]),(ys,ye))):
                canFall = False
                support[k].append(i)
        if not canFall:
            break
        zs -= 1
        ze -= 1
    done.append(((xs,ys,zs),(xe,ye,ze)))

p1 = 0
for k,block in enumerate(done):
    canBeDisintegrated = True
    for ke, it in support.items():
        if k in it and len(it) < 2:
            canBeDisintegrated = False
            break
    if canBeDisintegrated:
        p1 += 1
print(p1)