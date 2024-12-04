with open('in.txt') as f:
    grid = f.read().splitlines()
    
R = len(grid)
C = len(grid[0])
   
count = 0
# Horizontal
for line in grid:
    count += line.count('XMAS')
    count += line[::-1].count('XMAS')
    
# Vertical
for c in range(C):
    col = ''.join([grid[r][c] for r in range(R)])
    count += col.count('XMAS')
    count += col[::-1].count('XMAS')
    
# Diagonal
i,j = 0,0
while i < R and j < C:
    diag = ''
    for k in range(min(R-i,j+1)):
        diag += grid[i+k][j-k]
    count += diag.count('XMAS')
    count += diag[::-1].count('XMAS')
    if j+1 == C:
        i += 1
    else:
        j += 1

i,j = 0,C-1
while i < R and j >= 0:
    diag = ''
    for k in range(min(R-i,C-j)):
        diag += grid[i+k][j+k]
    count += diag.count('XMAS')
    count += diag[::-1].count('XMAS')
    if j == 0:
        i += 1
    else:
        j -= 1


print(f'Part 1: {count}')

count = 0
for i, row in enumerate(grid[:-2]):
    for j,c in enumerate(row[:-2]):
        jj = j+2
        diag1 = ''
        diag2 = ''
        for k in range(3):
            diag1 += grid[i+k][jj+k]
            diag2 += grid[i+k][jj-k]
        if (diag1=='MAS' or diag1[::-1]=='MAS') and (diag2=='MAS' or diag2[::-1]=='MAS'):
            count += 1
            
print(f'Part 2: {count}')