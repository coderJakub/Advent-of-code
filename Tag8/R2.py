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
places = [i for i in dest if i[-1]=='A']
placesIdx= [dest.index(i) for i in places]
i=0
allZ=False
while not allZ:
    for instruction in instructions:
        i+=1
        for j,place in enumerate(places):
            if instruction=='L':
                places[j] = val[placesIdx[j]][0]
            if instruction=='R':
                places[j] = val[placesIdx[j]][1]
            placesIdx[j]=dest.index(places[j])
        allZ=True
        for k in places:
            if k[-1]!='Z':
                allZ=False
                break
        if allZ:
            break
            
print(i)