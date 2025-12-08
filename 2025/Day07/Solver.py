import sys
from collections import defaultdict

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = f.read().splitlines()

fb = content[0].find('S')
beams = defaultdict(int, {fb: 1})
p1 = 0

for i in range(1,len(content)):
    newBeams = defaultdict(int)
    for beam, am in beams.items():
        if content[i][beam] == '^':
            p1 += 1
            newBeams[beam+1] += am
            newBeams[beam-1] += am
        else:
            newBeams[beam] += am
    beams = newBeams.copy()

print(f'Part 1: {p1}')
print(f'Part 2: {sum(beams.values())}')