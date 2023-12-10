from sys import argv


with open(argv[1]) as f:
    data = f.read().splitlines()

instructions = data[0]
data = data[2:]
dest = [i.split(" =")[0] for i in data]
val = [i.split(" = ")[1].split(", ") for i in data]
for i in range(len(val)):
    val[i][0]=val[i][0][1:]
    val[i][1]=val[i][1][:-1]
place ='AAA'
placeIdx=dest.index('AAA')
i=0
while place!='ZZZ':
    for instruction in instructions:
        i+=1
        if instruction=='L':
            place = val[placeIdx][0]
        if instruction=='R':
            place = val[placeIdx][1]
        if place=='ZZZ':
            break
        placeIdx=dest.index(place)
print(i)