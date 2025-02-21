with open('in.txt') as f:
    content = f.read()

keys = []
locks = []

for block in content.split('\n\n'):
    if block.startswith('.'):
        keys.append(block.splitlines())
    else:
        locks.append(block.splitlines())
    
p1 = 0
for lock in locks:
    for key in keys:
        fit = True
        for lineK, lineL in zip(key, lock):
            for k,l in zip(lineK, lineL):
                if l == '#' and k == '#':
                    fit = False
                    break
            if not fit:
                break
        p1 += 1 if fit else 0

print(p1)