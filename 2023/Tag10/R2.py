from sys import argv

def getNextIdx(i,j):
    match content[i][j]:
        case '|':return [[i+1,j],[i-1,j]]
        case '-':return [[i,j+1],[i,j-1]]
        case 'J':return [[i-1,j],[i, j-1]]
        case 'L':return [[i-1,j],[i, j+1]]
        case '7':return [[i+1,j],[i, j-1]]
        case 'F':return [[i+1,j],[i, j+1]]
        case '.':return None

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

resArr=[['.' for _ in line] for line in content]
startCoords=[0,0]
for line, item in enumerate(content):
    if item.find('S')!=-1:
        startCoords=[line,item.index('S')]
        break
resArr[startCoords[0]][startCoords[1]]='#'
currElement=[-1,-1]

#get currElement
for i,j in [[startCoords[0]+1,startCoords[1]],[startCoords[0]-1,startCoords[1]],[startCoords[0],startCoords[1]+1],[startCoords[0],startCoords[1]-1]]:
    if 0<=i<len(content) and 0<=j<len(content[0]):
        n = getNextIdx(i,j)
        if n!=None and startCoords in n:
            currElement=[i,j]
            break


before = startCoords
#iterate from first way
while currElement!=startCoords:
    resArr[currElement[0]][currElement[1]]='#'
    sol=getNextIdx(currElement[0], currElement[1])
    if sol[0]==before:
        before=currElement
        currElement=sol[1]
    else:
        before=currElement
        currElement=sol[0]

fill(resArr)
for line in resArr:
    for item in line:
        print(item, end='')
    print()