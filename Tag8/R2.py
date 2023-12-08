from sys import argv
import math

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
i=[0]*len(places)
for j,place in enumerate(places):
    while place[-1]!='Z':
        for instruction in instructions:
            i[j]+=1
            if instruction=='L':
                place = val[placesIdx[j]][0]
            if instruction=='R':
                place = val[placesIdx[j]][1]
            if place[-1]=='Z':
                break
            placesIdx[j]=dest.index(place)
print(math.lcm(*i))