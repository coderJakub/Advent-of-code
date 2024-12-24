with open('in.txt') as f:
    content = f.read()

wires = {x.split(': ')[0]:int(x.split(': ')[1]) for x in content.split('\n\n')[0].splitlines()}
gates = []

for line in content.split('\n\n')[1].splitlines():
    line = line.split(' -> ')
    input = line[0].split(' ')
    gates.append([*input, line[1]])

while gates:
    x,g,y,z = gates.pop(0)
    if x not in wires or y not in wires:
        gates.append([x,g,y,z])
        continue
    match g:
        case 'AND': wires[z] = wires[x] & wires[y]
        case 'OR': wires[z] = wires[x] | wires[y]
        case 'XOR': wires[z] = wires[x] ^ wires[y]

outputKeys = []
for key in wires.keys():
    if key.startswith('z'):
        outputKeys.append(key)

num = ''
for key in sorted(outputKeys,reverse=True):
    num += str(wires[key])

print(f'Part 1: {int(num,2)}')