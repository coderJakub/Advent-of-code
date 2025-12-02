with open('in.txt') as f:
    content = f.read().split(",")
    
p1 = 0
p2 = 0

for idRange in content:
    a, b = list(map(int, idRange.split('-')))
    for id in range(a, b+1):
        idStr = str(id)
        lenID = len(idStr)
        for rLen in range(1, lenID//2+1):
            if lenID % rLen != 0: continue
            num1 = idStr[:rLen]
            if all(idStr[idx:idx+rLen]==num1 for idx in range(rLen, lenID, rLen)): 
                p2 += id
                break
        if idStr[:lenID//2] == idStr[lenID//2:]: p1 += id

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')