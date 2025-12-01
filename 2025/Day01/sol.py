with open('in.txt') as f:
    content = f.read().split("\n")
    
dial = 50
p1 = 0
p2 = 0

for line in content:
    k = line[0]
    l = int(line[1:])
    dial+=l if k=='R' else -l
    p2 += abs(int(dial/100)) + (dial<=0 and dial!=-l)
    dial%=100
    p1 += dial==0

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')