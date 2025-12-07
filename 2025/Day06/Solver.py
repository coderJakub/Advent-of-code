import sys

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = f.read().splitlines()
    grid = [line.split() for line in content]

p1 = 0

for j in range(len(grid[0])):
    mul = grid[-1][j]=='*'
    num = 1 if mul else 0
    for k in range(len(grid)-1):
        if mul: num*= int(grid[k][j])
        else: num+= int(grid[k][j])
    p1 += num
    
p2 = 0
idx = 0
operations = content[-1]
while idx<len(content[0]):
    mul = operations[idx]=='*'
    num = 1 if mul else 0
    while idx==len(content[0])-1 or (idx+1<len(content[0]) and operations[idx+1]==' '):
        currNum = ''
        for k in range(len(content)-1):
            if content[k][idx] != ' ': currNum += content[k][idx]
        if mul: num *= int(currNum)
        else: num += int(currNum)
        idx +=1
    idx+=1
    p2 += num
    
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')