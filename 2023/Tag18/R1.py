from sys import argv

with open(argv[1]) as f:
    content = f.read().splitlines()

field = [['#']]
col=0
row=0

def drawSteps(pos, x, v, st):
    for k in range(st):
        pos[x] = pos[x] + (1 if v=='+' else -1)
        field[pos[0]][pos[1]]='#'
    return pos

def doInstruction(i,row, col):
    d = i.split(" ")[0]
    st = int(i.split(" ")[1])
    
    if d == "R":
        for k in range(len(field)):
            for l in range(col+st+1-len(field[k])):
                field[k].append('.')
        row,col=drawSteps([row,col],1,'+',st)
    elif d=="L":
        for k in range(len(field)):
            for l in range(-(col-st)):
                field[k].insert(0,'.')
                col+=1
        row,col=drawSteps([row,col],1,'-',st)
    elif d=="U":
        for k in range(-(row-st)):
            field.insert(0,['.']*len(field[0]))
            row+=1
        row,col=drawSteps([row,col],0,'-',st)
    elif d=="D":
        for k in range(row+st+1-len(field)):
            field.append(['.']*len(field[0]))
        row,col=drawSteps([row,col],0,'+',st)
    return row,col

for i in content:
    row,col= doInstruction(i,row,col)
        
for i in range(len(field)):
    draw = False
    for j in range(len(field[i])):
        if field[i][j]=="#":
            pass
res=0
for i in field:
    res+=i.count('#')
print(res)