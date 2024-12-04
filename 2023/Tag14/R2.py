from sys import argv
from copy import deepcopy
with open(argv[1]) as f:
    content=f.read().splitlines()
content = [list(i) for i in content]

R = len(content)
C = len(content[0])

def cycle(content): 
    for _ in range(2):
        for xx,yy in [(-1,0),(0,-1)]:
            for row,dataR in enumerate(content):
                for col,dataC in enumerate(dataR):
                    if dataC=='O':
                        i,j = row+xx,col+yy
                        while i in range(R) and j in range(C):
                            if content[i][j] in ['#', 'O']:
                                break
                            i,j = i+xx,j+yy
                            
                        i,j = i-xx,j-yy
                        content[row][col] = '.'
                        content[i][j] = 'O'
        content = content[::-1]
        for i in range(C):
            content[i] = content[i][::-1]
    return content

cycles = [deepcopy(content)]
cycleLen=0
cycleStart=0
for i in range(1,1000000001):
    content = cycle(content)
    if content in cycles:
        cycleStart = cycles.index(content)
        cycleLen = i-cycleStart
        break
    cycles.append(deepcopy(content))

load = 0
for row,dataR in enumerate(cycles[(1000000000-cycleStart)%cycleLen+cycleStart]):
    load+=dataR.count("O")*(len(content)-row)
print(load)