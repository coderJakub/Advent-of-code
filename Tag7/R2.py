from sys import argv

cardsVal  = {"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"J":-1,"Q":10,"K":11,"A":12}
def getValue(c):
    arr =[0]*13
    for i in c:
        arr[cardsVal[i]]+=1
    arr.sort(reverse=True)
    if arr[0]==5:
        return 7
    if arr[0]==4:
        return 6
    if arr[0]==3 and arr[1]==2:
        return 5
    if arr[0]==3:
        return 4
    if arr[0]==2 and arr[1]==2:
        return 3
    if arr[0]==2:
        return 2
    else:
        return 1

def compare(c1,c2):
    v1=getValue(c1)
    v2=getValue(c2)
    if v1<v2:
        return True
    elif v1>v2:
        return False
    for i in range(len(c1)):
        if cardsVal[c1[i]]<cardsVal[c2[i]]:
            return True
        elif cardsVal[c1[i]]>cardsVal[c2[i]]:
            return False
    return False

with open(argv[1]) as f:
    content = f.readlines()
cards = [i.split(" ") for i in content]

for i in range(len(cards)):
    for j in range(i,len(cards)):
        if not compare(cards[i][0],cards[j][0]):
            cards[i], cards[j] = cards[j], cards[i]
res=0
for i in range(len(cards)):
    res+=int(cards[i][1])*(i+1)
for i in cards:
    print(i[0])
print(res)