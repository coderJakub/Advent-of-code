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
        err=False
        while True:
            if 0<=row-dist<row+dist+1<len(pattern):
                if pattern[row-dist] != pattern[row+dist+1]:
                    err=True
                dist+=1
            else:
                break
        if not err:
            res+=(row+1)*100

    for row in range(len(pattern[0])-1):
        dist=0
        err=False
        while True:
            if 0<=row-dist<row+dist+1<len(pattern[0]):
                for k in range(len(pattern)):
                    if pattern[k][row-dist]!=pattern[k][row+dist+1]:
                        err=True
                dist+=1
            else: 
                break
        if not err:
            res+=row+1
            
print(res)
