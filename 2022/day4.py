from sys import argv

with open(argv[1]) as f:
    content=f.read().splitlines()

def includes(i1,i2):
    i1=[int(i) for i in i1.split("-")]
    i2=[int(i) for i in i2.split("-")]
    if i1[0]<=i2[0] and i1[1]>=i2[1]:
        return True
    if i1[0]>=i2[0] and i1[1]<=i2[1]:
        return True
    return False
def overlaps(i1,i2):    
    i1=[int(i) for i in i1.split("-")]
    i2=[int(i) for i in i2.split("-")]
    i2 = [i for i in range(i2[0], i2[1]+1)]
    for i in range(i1[0], i1[1]+1):
        if i in i2:
            return True
    return False
res1=0
res2=0
for pair in content:
    pair1=pair.split(",")[0]
    pair2=pair.split(",")[1]
    if includes(pair1, pair2):
        res1+=1
        res2+=1
        continue
    if overlaps(pair1, pair2):
        res2+=1
print(res1)
print(res2)