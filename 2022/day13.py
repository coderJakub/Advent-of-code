from sys import argv
from functools import cmp_to_key

def checkInt(i): # stattdessen auch isinstance(i, int) möglich
    try:
        int(i)
        return True
    except:
        return False
def compareLists(l1 ,l2):
    for i, item1 in enumerate(l1):
        if i>=len(l2):
            return 1
        item2 = l2[i]
        if checkInt(item1) and checkInt(item2):
            if item1==item2:
                continue
            return -1 if item1<item2 else 1
        elif not checkInt(item1) and not checkInt(item2):
            cl = compareLists(item1, item2)
            if cl == 0:
                continue
            return cl
        else:
            if checkInt(item1):
                cl = compareLists([item1], item2)
            else:
                cl = compareLists(item1, [item2])
            if cl == 0:
                continue
            return cl
    if not len(l1)==len(l2):
        return -1
    return 0

def readList(l):
    ret = []
    while True:
        l = l[1:]
        if l[0] == ',':
            continue
        if l[0] == ']':
            return ret, l
        if l[0].isdigit():
            if not l[1].isdigit():
                ret.append(int(l[0]))
            else:
                ret.append(int(l[0:2]))
                l = l[1:]

        else:
            r,l = readList(l)
            ret.append(r)    

with open(argv[1]) as f:
    content = f.read()

count = 0
allLists = []
for i,vgl in enumerate(content.split('\n\n')):
    l1 = readList(vgl.split('\n')[0])[0] # oder eval(vgl.split...) -> übersetzt automatisch in Liste
    l2 = readList(vgl.split('\n')[1])[0]
    allLists.append(l1)
    allLists.append(l2)
    if compareLists(l1,l2)==-1:
        count += i+1
print(f'Part 1: {count}')

allLists.append([[2]])
allLists.append([[6]])

allLists = sorted(allLists, key=cmp_to_key(compareLists))
idx1 = allLists.index([[2]])+1
idx2 = allLists.index([[6]])+1
print(f'Part 2: {idx1*idx2}')