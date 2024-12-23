from collections import defaultdict
with open('in.txt') as f:
    content = [list(x.split('-')) for x in f.read().splitlines()]

computers = set()
connections = defaultdict(set)
for line in content:
    computers.add(line[0])
    computers.add(line[1])
    connections[line[0]].add(line[1])
    connections[line[1]].add(line[0])

p1 = 0
for i,line in enumerate(content):
    groups = defaultdict(set)
    for j,line2 in enumerate(content[i+1:]):
        if line2[0] in line:
            groups[line2[1]].add(line2[0])
        if line2[1] in line:
            groups[line2[0]].add(line2[1])
    p1 += sum(len(val)==2 and (k.startswith('t') or list(val)[0].startswith('t') or list(val)[1].startswith('t')) for k,val in groups.items())
print(f'Part 1: {p1}')

computers = list(computers)
best = set()
for i,comp1 in enumerate(computers):
    currentGroup = set([comp1])
    for j,comp2 in enumerate(computers[i+1:]):
        if all(comp2 in connections[x] for x in currentGroup):
            currentGroup.add(comp2)
    if len(currentGroup) > len(best):
        best = currentGroup
        
best = list(best)
best.sort()
print(f'Part 2: {','.join(best)}')