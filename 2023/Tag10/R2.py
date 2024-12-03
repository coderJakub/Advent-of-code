from sys import argv
import sys
sys.setrecursionlimit(10**6)

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
            elif grid[r][c] == 'o':
                grid[r][c] = '.'

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

following = currElement
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

#find pice for S
s = None
for p in ['|','-','7','F','J','L']:
    content[startCoords[0]] = content[startCoords[0]][:startCoords[1]]+p+content[startCoords[0]][startCoords[1]+1:]
    n = getNextIdx(startCoords[0],startCoords[1])
    if n.count(following)!=0 and n.count(before)!=0:
        s = p
        break

# Inspired by https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/10.py
R = len(content)
C = len(content[0])
R2 = 3*R
C2 = 3*C
grid2 = [['.' for _ in range(C2)] for _ in range(R2)]
for r in range(R):
  for c in range(C):
    if resArr[r][c] == '#':
        if content[r][c]=='|':
            grid2[3*r+0][3*c+1] = 'x'
            grid2[3*r+1][3*c+1] = 'x'
            grid2[3*r+2][3*c+1] = 'x'
        elif content[r][c]=='-':
            grid2[3*r+1][3*c+0] = 'x'
            grid2[3*r+1][3*c+1] = 'x'
            grid2[3*r+1][3*c+2] = 'x'
        elif content[r][c]=='7':
            grid2[3*r+1][3*c+0] = 'x'
            grid2[3*r+1][3*c+1] = 'x'
            grid2[3*r+2][3*c+1] = 'x'
        elif content[r][c]=='F':
            grid2[3*r+2][3*c+1] = 'x'
            grid2[3*r+1][3*c+1] = 'x'
            grid2[3*r+1][3*c+2] = 'x'
        elif content[r][c]=='J':
            grid2[3*r+1][3*c+0] = 'x'
            grid2[3*r+1][3*c+1] = 'x'
            grid2[3*r+0][3*c+1] = 'x'
        elif content[r][c]=='L':
            grid2[3*r+0][3*c+1] = 'x'
            grid2[3*r+1][3*c+1] = 'x'
            grid2[3*r+1][3*c+2] = 'x'
    elif resArr[r][c]=='.':
      pass
  
fill(grid2)
count=0
for i,line in enumerate(resArr):
    for j,item in enumerate(line):
        inPipe = True
        for rr in range(3):
            for cc in range(3):
                if grid2[3*i+rr][3*j+cc]!='#':
                    inPipe = False
        if inPipe:
            count+=1
print(count)