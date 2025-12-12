import sys
from math import prod

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = f.read().split("\n\n")

tiles = [sum(c=='#' for row in block.splitlines()[1:] for c in row) for block in content[:-1]]

p1 = 0
for region in content[-1].splitlines():
    size, shapeList = region.split(": ")
    size = prod(map(int, size.split('x')))
    shapeList = map(int, shapeList.split())
    
    if size >= sum(tiles[i]*am for i, am in enumerate(shapeList)):
        p1 += 1

print("Part 1:", p1)
print("Part 2: collect all stars")