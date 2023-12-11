from sys import argv

with open(argv[1]) as f:
    content = f.read().splitlines()

galaxies=[]
col=[]
line=[]
first = True
foundGalaxy=True
for i in range(len(content[0])):
    if not foundGalaxy:
        foundGalaxy = True
        continue
    foundGalaxy=False
    
    for j in range(len(content)):
        if first and '#' not in content[j]:
            line.append(j)
        if content[j][i]=='#':
            foundGalaxy=True
    if first:
        first=False
    if not foundGalaxy:
        col.append(i)
    else:
        foundGalaxy=True

for i,line in enumerate(content):
    for j,char in enumerate(line):
        if char=='#':
            galaxies.append([i,j])

res=0
for i,galaxy in enumerate(galaxies):
    for j in range(i+1,len(galaxies)):
        res+=abs(galaxy[0]-galaxies[j][0])+abs(galaxy[1]-galaxies[j][1])
        #add expension
print(res)