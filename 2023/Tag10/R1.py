from sys import argv

def getNextIdx(i,j):
    if content[i][j]=='|':
        return [[i+1,j],[i-1,j]]
    elif content[i][j]=='-':
        return [[i,j+1],[i,j-1]]
    elif content[i][j]=='J':
        return [[i-1,j], [i, j-1]]
    elif content[i][j]=='L':
        return [[i-1,j], [i, j+1]]
    elif content[i][j]=='7':
        return [[i+1,j], [i, j-1]]
    elif content[i][j]=='F':
        return [[i+1,j], [i, j+1]]
    elif content[i][j]=='S' or content[i][j]=='.':
        return None

with open(argv[1]) as f:
    content = f.read().splitlines()

resArr=[[-1 for j in range(len(content[i]))] for i in range(len(content))]
lineIdx=0
itemIdx=0
for line, item in enumerate(content):
    if item.find('S')!=-1:
        lineIdx=line
        itemIdx=item.index('S')
        break
resArr[lineIdx][itemIdx]=0
start1=[-1,-1]
start2=[-1,-1]

#get start1 and start2
for i in range(lineIdx-1, lineIdx+2):
    for j in range(itemIdx-1, itemIdx+2):
        if i>=0 and j>=0 and i<len(content) and j<len(content[0]):
            x = getNextIdx(i,j)
            if x!=None and [lineIdx, itemIdx] in x and start1==[-1,-1]:
                start1=[i,j]
            elif x!=None and [lineIdx, itemIdx] in x:
                start2=[i,j]
                break
print("[",lineIdx, itemIdx,"]",start1, start2)
i=1
before = [lineIdx, itemIdx]
#iterate from first way
while start1!=start2:
    resArr[start1[0]][start1[1]]=i
    i+=1
    sol=getNextIdx(start1[0], start1[1])
    if sol[0]==before:
        before=start1
        start1=sol[1]
    else:
        before=start1
        start1=sol[0]
resArr[start1[0]][start1[1]]=i
i=1
before = [lineIdx, itemIdx]
#iterate from second way
print(resArr[start2[0]][start2[1]])
while resArr[start2[0]][start2[1]]>i:
    resArr[start2[0]][start2[1]]=i
    i+=1
    sol=getNextIdx(start2[0], start2[1])
    if sol[0]==before:
        before=start2
        start2=sol[1]
    else:
        before=start2
        start2=sol[0]
x =-1
for k in resArr:
    if x<max(k):
        x=max(k)
print(x)