import sys

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    grid = [list(line) for line in f.read().splitlines()]

R = len(grid)
C= len(grid[0])

def getAdjRools(i, j, grid):
    adj = 0
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            ni, nj = i+ii, j+jj
            adj += 0<=ni<R and 0<=nj<C and (ii,jj) != (0,0) and grid[ni][nj] == '@'
    return adj

p1 = 0
p2 = 0

changes = True
rounds = 0
while changes:
    changes = False
    removable = set()
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c=='@' and getAdjRools(i, j, grid) < 4:
                removable.add((i,j))
    
    for i, j in removable: grid[i][j] = '.'
    if rounds == 0: p1 = len(removable)
    p2 += len(removable)
    changes = len(removable)>0
    rounds += 1
    
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')