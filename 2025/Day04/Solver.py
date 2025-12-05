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
firstRound = True
while changes:
    changes = False
    removable = set()
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c=='@' and getAdjRools(i, j, grid) < 4:
                changes = True
                p1 += firstRound
                if not firstRound:
                    grid[i][j] = '.'
                    p2 += 1
    firstRound = False
    
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')