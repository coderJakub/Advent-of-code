from sys import argv

def getNextIdx(i,j):
    match content[i][j]:
        case '|':return [[i+1,j],[i-1,j]]
        case '-':return [[i,j+1],[i,j-1]]
        case 'J':return [[i-1,j],[i, j-1]]
        case 'L':return [[i-1,j],[i, j+1]]
        case '7':return [[i+1,j],[i, j-1]]
        case 'F':return [[i+1,j],[i, j+1]]
        case _:return None

with open(argv[1]) as f:
    content = f.read().splitlines()

resArr=[[-1 for j in range(len(content[i]))] for i in range(len(content))]
startCoords=[0,0]
for line, item in enumerate(content):
    if item.find('S')!=-1:
        startCoords=[line,item.index('S')]
        break
resArr[startCoords[0]][startCoords[1]]=0
currElement=[-1,-1]

#get currElement
for i in range(startCoords[0]-1, startCoords[0]+2):
    for j in range(startCoords[1]-1, startCoords[1]+2):
        if i>=0 and j>=0 and i<len(content) and j<len(content[0]):
            if startCoords in getNextIdx(i,j):
                currElement=[i,j]
                break

i=1
before = startCoords
#iterate from first way
while currElement!=startCoords:
    resArr[currElement[0]][currElement[1]]=i
    i+=1
    sol=getNextIdx(currElement[0], currElement[1])
    if sol[0]==before:
        before=currElement
        currElement=sol[1]
    else:
        before=currElement
        currElement=sol[0]
resArr[currElement[0]][currElement[1]]=i

print(resArr[startCoords[0]][startCoords[1]]//2)