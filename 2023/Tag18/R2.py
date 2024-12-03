import sys
from sys import argv
sys.setrecursionlimit(10**6)

with open(argv[1]) as f:
    content = f.read().splitlines()

def fill(grid):
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == '.'

    def mark_outside(x, y):
        if not is_valid(x, y):
            return
        grid[x][y] = 'o'
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            mark_outside(x + dx, y + dy)

    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == '.':
                mark_outside(r, c)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                grid[r][c] = '#' 
                
grid = set()
grid.add((0,0))
i,j = 0,0
for inst in content:
    hexa = inst.split(" ")[2][2:-1]
    hexa_str = '0x'+hexa[:-1]
    d = hexa[-1]
    st = int(hexa_str, 16)
    match int(d):
        case 0:
            dir = [0,1]
        case 2:
            dir = [0,-1]
        case 3:
            dir = [-1,0]
        case 1:
            dir = [1,0]
        
    for _ in range(st):
        i+=dir[0]
        j+=dir[1]
        grid.add((i,j))
      
      
x_min = min([x[0] for x in grid])
y_min = min([x[1] for x in grid])
x_max = max([x[0] for x in grid])
y_max = max([x[1] for x in grid])

field = [['#' if (i,j) in grid else '.' for j in range(y_min,y_max+1)] for i in range(x_min,x_max+1)]
fill(field)

count = 0
for line in field:
    for c in line:
        if c == '#':
            count +=1

print(count)