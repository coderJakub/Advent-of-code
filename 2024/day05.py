from collections import defaultdict
with open('in.txt') as f:
    content = f.read()

def checkRow(instr):
    updt = []
    for i,k in enumerate(instr):
        if k not in ab:
            updt.append(k)
        else: 
            if not all([abh in updt for abh in ab[k] if abh in instr]):
                return False,[abh for abh in ab[k] if abh in instr and abh not in updt],i
            updt.append(k)
    return True, None, None

def correctInstr(instr,wrong,index):
    while True:
        for w in wrong:
            instr.remove(w)
            instr.insert(index,w)  
        r,wrong,index = checkRow(instr)
        if r:
            return int(instr[len(instr)//2])

ab = defaultdict(list)
inst = content.split('\n\n')[1].splitlines()
for row in content.split('\n\n')[0].splitlines():
    v,k = row.split('|')
    ab[k].append(v)

p1=0
p2=0
for i,line in enumerate(inst):
    instr = line.split(',')
    rightOrd,w,idx = checkRow(instr)
    if rightOrd:
        p1 +=int(instr[len(instr)//2])
    else:
        p2 += correctInstr(instr,w,idx)
    
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')