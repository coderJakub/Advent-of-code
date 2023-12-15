from sys import argv

with open(argv[1]) as f:
    content=f.read().splitlines()

def findDoubles(s1, s2):
    doubles=""
    for c in s1:
        if s2.count(c)!=0:
            doubles+=c
    return doubles

doubles=""
for ruck in content:
        sec = ruck[len(ruck)//2:]
        k=list(ruck[:len(ruck)//2])
        k=list(dict.fromkeys(k))
        doubles+=findDoubles(k,sec)

badges=""     
for i in range(0,len(content),3):
    for k in range(i,i+3):
        content[k]=list(dict.fromkeys(content[k]))
    doubles=findDoubles(content[i], content[i+1])
    badges+=findDoubles(doubles, content[i+2])

print(badges)
for part2 in [False, True]:
    res=0
    for i in (doubles if not part2 else badges):
        if 97<=ord(i)<=122:
            res+=(ord(i)-96)
        else:
            res+=(ord(i)-38)
    print(res)