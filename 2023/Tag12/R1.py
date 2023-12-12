from sys import argv
import itertools

def getPosib(group, numbers):
    posib=0
    n=group.count('?')
    l = list(itertools.product(["#","."], repeat=n))
    for i in l:
        k=0
        newGroup=group
        for j, char in enumerate(newGroup):
            if char == "?":
                newGroup = newGroup[:j] + i[k] + newGroup[j + 1:]
                k+=1
        if isValid(newGroup, numbers):
            posib+=1
    return posib

def isValid(group, numbers):
    damaged = group.split(".")
    damaged=list(filter(lambda x: x != '', damaged))
    if(len(damaged)!=len(numbers)):
        return False
    for i,n in enumerate(numbers):
        if(n!=len(damaged[i])):
            return False
    return True

with open(argv[1]) as f:
    content = f.read().splitlines()
groups = [i.split(" ")[0] for i in content]
numbers = [[int(j) for j in i.split(" ")[1].split(",")]for i in content]

res=0
for i,group in enumerate(groups):
    res+=getPosib(group, numbers[i])
print(res)