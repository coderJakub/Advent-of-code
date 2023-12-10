from sys import argv

def getNum(data, line, char):
    while char>=0 and data[line][char].isnumeric():
        char-=1
    char+=1
    res=""
    start=char
    while char<len(data[line]) and data[line][char].isnumeric():
        res+=data[line][char]
        char+=1
    return [int(res), start, char]

def check(line, char,data):
    firstNum=[-1,0,0]
    secondNum=[-1,0,0]
    for i in range(line-1, line+2):
        for j in range(char-1, char+2):
            if i>=0 and i<len(data) and j>=0 and j<len(data[i]):
                if data[i][j].isnumeric():
                    if firstNum[0]==-1:
                        firstNum=getNum(data,i,j)
                    else:
                        secondNum=getNum(data,i,j)  
                        if secondNum!=firstNum:
                            return secondNum[0]*firstNum[0]   
    return 0

with open(argv[1]) as f:
    lines = f.readlines()
res=0
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c == "*":
            res+=check(i,j,lines)
        
print(res)