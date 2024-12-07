from sys import argv
from copy import deepcopy

with open(argv[1]) as f:
    content = f.read()

fp = content.split('\n\n')[0]

workflows = {line.split('{')[0]:line[:-1].split('{')[1] for line in fp.splitlines()}
idx = {'x':0, 'm':1, 'a':2, 's':3}

queue = [['in', [[1,4000],[1,4000],[1,4000],[1,4000]]]]

accepeted = []

while queue:
    s,inter = queue.pop(0)
    conditional = workflows[s].split(',')[:-1]
    last = workflows[s].split(',')[-1]   
    possible = True 
    for newS in conditional:
        cond,n = newS.split(':')
        temp = deepcopy(inter)
        if '>' in cond:
            i = idx[cond.split('>')[0]]
            temp[i][0] = max(inter[i][0],int(cond.split('>')[1])+1)
            inter[i][1] = min(inter[i][1],int(cond.split('>')[1])) 
        elif '<' in cond:
    
            i = idx[cond.split('<')[0]] 
            temp[i][1] = min(inter[i][1],int(cond.split('<')[1])-1)
            inter[i][0] = max(inter[i][0],int(cond.split('<')[1]))
        if n == 'A':
            accepeted.append(temp)
        elif n != 'R' and temp[i][0]<=temp[i][1]:
            queue.append([n,temp])
        if inter[i][0]>inter[i][1]:
            possible = False
            break
    if not possible:
        continue
    if last == 'A':
        accepeted.append(inter)
    elif last != 'R':
        queue.append([last,inter])
count =0
for a in accepeted:
    c = 1
    for i in range(4):
        c *= a[i][1]-a[i][0]+1
    count += c
print(count)