from collections import defaultdict
with open('in.txt') as f:
    content = f.read()
    
line = {int(x):1 for x in content.split(" ")}


for k in range(75):
    if k==25:
        print(f'Part 1: {sum([x for _,x in line.items()])}')
    newLine = line.copy()
    
    line = defaultdict(int)
    for x in newLine:
        if x == 0:
            line[1] += newLine[x]
        elif len(str(x))%2==0:
            line[int(str(x)[:len(str(x))//2])] += newLine[x]
            line[int(str(x)[len(str(x))//2:])] += newLine[x]
        else:
            line[x*2024] += newLine[x]

print(f'Part 2: {sum([x for _,x in line.items()])}')