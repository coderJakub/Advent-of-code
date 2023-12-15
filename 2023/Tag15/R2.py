from sys import argv

with open(argv[1]) as f:
    content = f.read()

def hashFunc(string):
    return ((ord(string[-1])+hashFunc(string[:-1]))*17)%256 if len(string)!=1 else (ord(string[0])*17)%256

def getIndex(idx,string):
    for i,element in enumerate(box[idx]):
        if element[0]==string:
            return i
    return -1

box = [[] for _ in range(256)]
for string in content.split(","):
    if string.count("=")!=0:
        temp=string.split("=")
        idx = hashFunc(temp[0])
        if len(box[idx])==0:
            box[idx]=[[temp[0], int(temp[1])]]
        else:
            i=getIndex(idx,temp[0])
            if i!=-1:
                box[idx][i][1]=int(temp[1])
            else:
                box[idx].append([temp[0], int(temp[1])])
    if string.count("-")!=0:
        string=string.split("-")[0]
        idx = hashFunc(string)
        i=getIndex(idx, string)
        if i!=-1:
            box[idx].pop(i)
res=0
for i in range(len(box)):
    for j, el in enumerate(box[i]):
        k=res
        res+=(i+1)*(j+1)*el[1]
print(res)