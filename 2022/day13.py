from sys import argv

def checkInt(i):
    try:
        int(i)
        return True
    except:
        return False
def compareLists(l1 ,l2):
    for i, item1 in enumerate(l1):
        if i>=len(l2):
            return False
        item2 = l2[i]
        if checkInt(item1) and checkInt(item2):
            if item1==item2:
                continue
            return item1<item2
        elif not checkInt(item1) and not checkInt(item2):
            cl = compareLists(item1, item2)
            if cl == None:
                continue
            return cl
        else:
            if checkInt(item1):
                cl = compareLists([item1], item2)
            else:
                cl = compareLists(item1, [item2])
            if cl == None:
                continue
            return cl
    if not len(l1)==len(l2):
        return True    

with open(argv[1]) as f:
    content = f.read()

count = 0
for i,vgl in enumerate(content.split('\n\n')):
    l1 = eval(vgl.split('\n')[0])
    l2 = eval(vgl.split('\n')[1])
    print(l1)
    print(l2)
    print(compareLists(l1,l2))
    print()
    if compareLists(l1,l2):
        count += i+1
print(count)