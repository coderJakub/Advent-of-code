from sys import argv

with open(argv[1]) as f:
    content = f.read().splitlines()

col=[]
row=[]
checkRows = True
foundGalaxy=False
for i in range(len(content[0])):
    foundGalaxy=False
    
    for j in range(len(content)):
        if checkRows and '#' not in content[j]:
            row.append(j)
        if content[j][i]=='#':
            foundGalaxy=True
    if checkRows:
        checkRows=False
    if not foundGalaxy:
        col.append(i)

galaxies=[]
for i,line in enumerate(content):
    for j,char in enumerate(line):
        if char=='#':
            galaxies.append([i,j])

res=0
for i,galaxy in enumerate(galaxies):
    for j in range(i+1,len(galaxies)):
        res+=abs(galaxy[0]-galaxies[j][0])+abs(galaxy[1]-galaxies[j][1])
        for k in col:
            if k>=min(galaxy[1], galaxies[j][1]) and k<=max(galaxy[1],galaxies[j][1]):
                res+=1000000-1
        for k in row:
            if k>=min(galaxy[0], galaxies[j][0]) and k<=max(galaxy[0],galaxies[j][0]):
                res+=1000000-1
print(res)