from collections import defaultdict
with open('in.txt') as f:
    lines = f.read().splitlines()

R=len(lines)
C=len(lines[0])

d = defaultdict(list)
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c!='.':
            d[c].append((i,j))

p1 = set()
p2 = set()
for k, it in d.items():
    for i in range(len(it)):
        for j in range(i+1,len(it)):
            a = it[i]
            b = it[j]
            ii,jj = b[0]-a[0],b[1]-a[1]
            for x,di,dj in ((a,-ii,-jj),(b,ii,jj)):
                if 0<=x[0]+di<R and 0<=x[1]+dj<C:
                    p1.add((x[0]+di,x[1]+dj))
                while 0<=x[0]<R and 0<=x[1]<C:
                    p2.add(x)
                    x = (x[0]+di,x[1]+dj)

print(f'Part 1: {len(p1)}')
print(f'Part 2: {len(p2)}')