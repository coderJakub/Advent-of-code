with open('in.txt') as f:
    content = f.read()

wires = {x.split(': ')[0]:int(x.split(': ')[1]) for x in content.split('\n\n')[0].splitlines()}
gates = {}
gatesList = []

for line in content.split('\n\n')[1].splitlines():
    line = line.split(' -> ')
    input = line[0].split(' ')
    gatesList.append([*input, line[1]])
    gates[line[1]] = [*input]

def runGates(wires, gates:dict):
    gatesList = []
    for k,(x,g,y) in gates.items():
        gatesList.append([x,g,y,k])
    while gatesList:
        x,g,y,z = gatesList.pop(0)
        if x not in wires or y not in wires:
            gatesList.append([x,g,y,z])
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
    return int(num,2)

print(f'Part 1: {runGates(wires, gates)}')

def getWrongBits():
    for i in range(45): 
        for k in range(45):           
            wires = {}
            x = 1<<i
            y = 1<<k
            for j in range(45):
                wires[f'x{j:02}'] = 1 if k==j else 0
                wires[f'y{j:02}'] = 1 if i==j else 0
            z = runGates(wires, gates)
            if z != x+y:
                print(x,y,z,i,k)
                #exit()

def printBit(gate,d=0):
    if d>3 or gate not in gates.keys():
        return
    x,g,y = gates[gate]
    print(' '*d, f'{gate} -> {x} {g} {y}')
    printBit(x,d+1)
    printBit(y,d+1)

switches = [['hbs','kfp'],['z18','dhq'],['z22','pdg'],['z27','jcp']]
switchWires = []
for switch in switches:
    x1,g1,y1 = gates[switch[0]]
    x2,g2,y2 = gates[switch[1]]
    gates[switch[0]], gates[switch[1]] = gates[switch[1]], gates[switch[0]]
    switchWires.extend(switch)
#getWrongBits()
#printBit('z28')
print(f'Part 2: {",".join(sorted(switchWires))}')