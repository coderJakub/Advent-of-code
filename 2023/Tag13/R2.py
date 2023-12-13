from sys import argv

with open(argv[1]) as f:
    data=f.read()
data = data.split("\n\n")

for i in range(len(data)):
    data[i] = data[i].splitlines()
    
res=0
for pattern in data:
    for row in range(len(pattern)-1):
        dist=0
        smudge=0
        while True:
            if 0<=row-dist<row+dist+1<len(pattern):
                for k in range(len(pattern[0])):
                    if pattern[row-dist][k]!=pattern[row+dist+1][k]:
                        smudge+=1
                dist+=1
            else:
                break
        if smudge==1:
            res+=(row+1)*100

    for row in range(len(pattern[0])-1):
        dist=0
        smudge=0
        while True:
            if 0<=row-dist<row+dist+1<len(pattern[0]):
                for k in range(len(pattern)):
                    if pattern[k][row-dist]!=pattern[k][row+dist+1]:
                        smudge+=1
                dist+=1
            else: 
                break
        if smudge==1:
            res+=row+1  
print(res)