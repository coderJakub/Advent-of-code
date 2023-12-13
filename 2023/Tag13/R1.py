from sys import argv

with open(argv[1]) as f:
    data=f.read()
data = data.split("\n\n")

for i in range(len(data)):
    data[i] = data[i].splitlines()
res=0
for content in data:
    for i in range(len(content)-1):
        j=0
        err=False
        while True:
            if 0<=i-j<i+j+1<len(content):
                if content[i-j] != content[i+j+1]:
                    err=True
                j+=1
            else:
                break
        if not err:
            res+=(i+1)*100

    for i in range(len(content[0])-1):
        j=0
        err=False
        while True:
            if 0<=i-j<i+j+1<len(content[0]):
                for k in range(len(content)):
                    if content[k][i-j]!=content[k][i+j+1]:
                        err=True
                j+=1
            else: 
                break
        if not err:
            res+=i+1
            
print(res)
