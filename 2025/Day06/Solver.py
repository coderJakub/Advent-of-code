import sys

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    contet = f.read()
    p1G = [line.split() for line in contet.splitlines()]
    p2G = contet.splitlines()

p1 = 0

for j in range(len(p1G[0])):
    mul = p1G[-1][j]=='*'
    num = 1 if mul else 0
    for k in range(len(p1G)-1):
        if mul: num*= int(p1G[k][j])
        else: num+= int(p1G[k][j])
    p1 += num
    
p2 = 0
idx = 0
operations = p2G[-1]
while idx<len(p2G[0]):
    mul = p1G[-1][j]=='*'
    num = 1 if mul else 0
    while idx==len(p2G[0])-1 or (idx+1<len(p2G[0]) and operations[idx+1]==' '):
        currNum = ''
        for k in range(len(p2G)-1):
            if p2G[k][idx] != ' ': currNum += p2G[k][idx]
        if mul: num *= int(currNum)
        else: num += int(currNum)
        idx +=1
    idx+=1
    p2 += num
    
print(p1)
print(p2)