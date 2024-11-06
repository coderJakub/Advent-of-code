from sys import argv
import math
with open(argv[1]) as f:
    content=f.read().splitlines()

field = [[0 for _ in range(len(content[j]))]for j in range(len(content))]

def getShortestWay(curr, d, straight,seen):
    if curr in seen or  curr[0]<0 or curr[1]<0 or curr[0]>=len(content) or curr[1]>=len(content[0]):
        return math.inf
    k=[i for i in seen]
    k.append(curr)
    if curr == [len(content)-1, len(content[0])-1]:
        print("ey")
        return int(content[-1][-1])
    way=[]
    direc=[[0,1],[1,0],[-1,0],[0,-1]]
    direc.pop(direc.index(d))
    direc.pop(direc.index([-d[0],-d[1]]))
    if straight!=3:
        way.append(getShortestWay([curr[0]+d[0], curr[1]+d[1]], d, straight+1,k))
    for i in range(2):
        way.append(getShortestWay([curr[0]+direc[i][0], curr[1]+direc[i][1]], direc[i], 1,k))
    return min(way)+int(content[curr[0]][curr[1]])
    
    
print(getShortestWay([0,0],[0,1], 1,[]))