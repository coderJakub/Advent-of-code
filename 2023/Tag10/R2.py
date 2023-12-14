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
def touch(i,j):
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if not(k>=0 and l>=0 and k<len(content) and l<len(content[0])):
                return True
            elif resArr[k][l]=='-':
                return True
    return False
    
with open(argv[1]) as f:
    content = f.read().splitlines()

resArr=[['0' for j in range(len(content[i]))] for i in range(len(content))]
lineIdx=0
itemIdx=0
for line, item in enumerate(content):
    if item.find('S')!=-1:
        lineIdx=line
        itemIdx=item.index('S')
        break
resArr[lineIdx][itemIdx]='x'
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
before = [lineIdx, itemIdx]
#iterate from first way
while start1!=[lineIdx, itemIdx]:
    resArr[start1[0]][start1[1]]='x'
    sol=getNextIdx(start1[0], start1[1])
    if sol[0]==before:
        before=start1
        start1=sol[1]
    else:
        before=start1
        start1=sol[0]

while True:
    changes = False
    for i in range(len(resArr)):
        for j in range(len(resArr[0])):
            if resArr[i][j]=='0' and touch(i,j):
                resArr[i][j]='-'
                changes=True
    if not changes:
        break
res=0
for i in resArr:
    print(i)
    res+=i.count(".")
print(res)