from sys import argv

def rowIsReflected(line, abst):
    if line-abst<0 or line+1+abst>=len(content):
        return False
    if content[line-abst] == content[line+abst+1]:
        return True
    return False

def colIsReflected(col,abst):
    if col-abst<0 or col+abst+1>=len(content[0]):
        return False
    for i in range(len(content)):
        if content[i][col-abst]!=content[i][col+abst+1]:
            return False
    return True

with open(argv[1]) as f:
    data=f.read()
data = data.split("\n\n")
for i in range(len(data)):
    data[i] = data[i].splitlines()
res=0
for content in data:
    col=[0,0]
    row=[0,0]
    for i in range(len(content)-1):
        j=0
        while rowIsReflected(i,j):
            j+=1
        row =[j,i] if j>row[0] else row

    for i in range(len(content[0])-1):
        j=0
        while colIsReflected(i,j):
            j+=1
        col =[j,i] if j>col[0] else col
    res+=col[1]+1 if col[0]>row[0] else (row[1]+1)*100
print(res)
