import sys

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    grid = f.read().split('\n\n')

fresh = [(tuple(map(int,line.split('-')))) for line in grid[0].splitlines()]
avialable = list(map(int, grid[1].splitlines()))

p1 = sum([any(rg[0]<=ingr<=rg[1] for rg in fresh) for ingr in avialable]) 

while True:
    newFresh = []
    for of in fresh:
        for i,nf in enumerate(newFresh):
            o1, o2 = of
            n1, n2 = nf
            if (n1<=o1<=n2) or (o1<=n1<=o2):
                newFresh[i] = (min(o1, n1), max(o2, n2))
                break
        else:
            newFresh.append(of)
    if newFresh == fresh: break
    fresh = newFresh.copy()

p2 = sum(i2-i1+1 for i1, i2 in fresh)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')