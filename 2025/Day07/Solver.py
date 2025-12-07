import sys
from collections import defaultdict

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = f.read().splitlines()

fb = content[0].find('S')

beams = defaultdict(int)
singleBeams = set([fb])
beams[fb] += 1
p1 = 0

for i in range(1,len(content)):
    newSingleBeams = set()
    newBeams = defaultdict(int)
    for beam in singleBeams:
        if content[i][beam] == '^':
            p1 += 1
            if beam+1<len(content):
                newSingleBeams.add(beam+1)
                newBeams[beam+1] += beams[beam]
            if beam-1>=0:
                newSingleBeams.add(beam-1)
                newBeams[beam-1] += beams[beam]
        else:
            newBeams[beam] += beams[beam]
            newSingleBeams.add(beam)
    beams = newBeams.copy()
    singleBeams = newSingleBeams.copy()

print(f'Part 1: {p1}')
print(f'Part 2: {sum(beams.values())}')