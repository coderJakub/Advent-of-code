from itertools import permutations
with open('in.txt') as f:
    content = f.read().splitlines()

coordsNumpad = {'7': (0,0),'8': (0,1),'9': (0,2),'4': (1,0),'5': (1,1),'6': (1,2),'1': (2,0),'2': (2,1),'3': (2,2),'0': (3,1),'A': (3,2)}   
coordsInstructionpad = {'^':(0,1), 'A':(0,2), '<':(1,0), 'v':(1,1), '>':(1,2)}
directions = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

def getPath(start,end,grid:dict):
    d_row = end[0] - start[0]
    d_col = end[1] - start[1]

    moves = ['^']*abs(d_row) if d_row < 0 else ['v']*d_row
    moves += ['<']*abs(d_col) if d_col < 0 else ['>']*d_col
    unique_paths = set(permutations(moves))

    valid_paths = []
    for path in unique_paths:
        current_position = start
        is_valid = True
        for move in path:
            current_position = (current_position[0] + directions[move][0], current_position[1] + directions[move][1])
            if current_position not in grid.values():
                is_valid = False
                break
        if is_valid:
            valid_paths.append(''.join(path)+'A')
    return valid_paths

def getInstructions(code,i,last,grid):
    global robot
    x,y = robot[i]
    instrString = ''
    for num in code:
        xx,yy = grid[num]
        bestString = ''
        possibleMoves = getPath((x,y),(xx,yy),grid)
        for k,moves in enumerate(possibleMoves):
            if i<2:
                moves = getInstructions(moves,i+1,k==len(possibleMoves)-1,coordsInstructionpad)
            if bestString=='' or len(moves)+1 < len(bestString):
                bestString = moves
        instrString += bestString
        x,y = xx,yy
    if last:
        robot[i] = (x,y)
    return instrString

p1 = 0 
robot = [coordsInstructionpad['A'] for _ in range(2)]
robot.insert(0,coordsNumpad['A'])
for line in content:
    numericPart = int(line[:-1])
    instr = getInstructions(line,0,True,coordsNumpad)
    p1 += numericPart*len(instr)

print(f'Part 1: {p1}')