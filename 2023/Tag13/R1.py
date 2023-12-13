from sys import argv

def rowIsReflected(line, abst):
    if line-abst<0 or line+1+abst>=len(content):
        return False
    if content[line-abst] == content[line+abst+1]:
        return True
    return False

def colIsReflected(col,abst):
    if col-abst<0 or col+abst+1>=len(content[1]):
        return False
    for i in range(len(content)):
        if content[i][col-abst]!=content[i][col+abst+1]:
            return False
    return True

with open(argv[1]) as f:
    content=f.read().splitlines()

res=0
for i in range(len(content)-1):
    j=0
    while rowIsReflected(i,j):
        j+=1
    res+=j

for i in range(len(content)[1]):
    j=0
    while colIsReflected(i,j):
        j+=1
    res+=j
print(res)
