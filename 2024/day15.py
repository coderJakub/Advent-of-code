with open('in.txt') as f:
    content = f.read()
    
gridP1 = [[c for c in line] for line in content.split('\n\n')[0].splitlines()]
instructions = content.split('\n\n')[1].strip()

gridP2 = []
for line in gridP1:
    newLine = []
    for c in line:
        if c == 'O':
            newLine.append('[')
            newLine.append(']')
        elif c == '.':
            newLine.append('.')
            newLine.append('.')
        elif c == '#':
            newLine.append('#')
            newLine.append('#')
        elif c == '@':
            newLine.append('@')
            newLine.append('.')
    gridP2.append(newLine)
DIR = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}
    
def tryToMove(coords,direction,grid):
    x,y = coords
    dx,dy = DIR[direction]
    if canMove(x,y,direction,grid):
        move(coords,direction,grid)
        return (x+dx,y+dy)
    return coords 

def move(coords, direction,grid):
    x,y = coords
    dx,dy = DIR[direction]
    if grid[x+dx][y+dy] == ']' and direction in '^v':
        move((x+dx,y+dy),direction,grid)
        move((x+dx,y+dy-1),direction,grid)
    elif grid[x+dx][y+dy] == '[' and direction in '^v':
        move((x+dx,y+dy),direction,grid)
        move((x+dx,y+dy+1),direction,grid)
    elif grid[x+dx][y+dy] in 'O[]':
        move((x+dx,y+dy),direction,grid)
    grid[x+dx][y+dy] = grid[x][y]
    grid[x][y] = '.'

def canMove(x,y,direction,grid):
    dx,dy = DIR[direction]
    if grid[x][y] == '.':
        return True
    if grid[x][y] == '#':
        return False
    if grid[x][y]==']' and direction in '^v':
        return canMove(x+dx,y,direction,grid) and canMove(x+dx,y-1,direction,grid)
    if grid[x][y]=='[' and direction in '^v':
        return canMove(x+dx,y,direction,grid) and canMove(x+dx,y+1,direction,grid)
    if grid[x][y] in '@O[]':
        return canMove(x+dx,y+dy,direction,grid)
    
for i,line in enumerate(gridP1):
    for j,c in enumerate(line):
        if c == '@':
            robot1 = (i,j)
            robot2 = (i,j*2)
            break

for instr in instructions:
    if instr not in "<>^v":
        continue
    robot1 = tryToMove(robot1,instr,gridP1)    
    robot2 = tryToMove(robot2,instr,gridP2)    

for p,grid in [('1',gridP1),('2',gridP2)]:
    count = 0
    for i,line in enumerate(grid):
        for j,c in enumerate(line):
            if c == 'O' or c == '[':
                count += 100*i+j
    print(f'Part {p}: {count}')