from sys import argv

def getPredictedVal(line):
    if all(p==0 for p in line):
        return 0
    newLine = []
    for i in range(len(line)-1):
        newLine.append(line[i+1]-line[i])
    pred=getPredictedVal(newLine)
    return line[0]-pred

with open(argv[1]) as f:
    data = f.read().splitlines()

res=0
for line in data:
    line = [int(i) for i in line.split(" ")]
    res+=getPredictedVal(line)
    print(res)