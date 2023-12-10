from sys import argv

def func(j,time):
    return j*(time-j)

with open(argv[1]) as f:
    content = f.readlines()

content[0]=content[0].split(": ")[1]
content[1]=content[1].split(": ")[1]
times=content[0].split(" ")
times=list(filter(lambda x: x != '', times))
distance=content[1].split(" ")
distance=list(filter(lambda x: x != '', distance))
times[-1]=times[-1].split("\n")[0]
distance[-1]=distance[-1].split("\n")[0]

res=1
timeS=""
distanceS=""
for i,time in enumerate(times):
    timeS+=time
    distanceS+=distance[i]
print(timeS, distanceS)
startB=0
endB=0
time=int(timeS)
distance=int(distanceS)
for j in range(int(time)):
    if func(j,int(time))>int(distance):
        startB=j
        break
for j in range(int(time),startB,-1):
    if func(j,int(time))>int(distance):
        endB=j
        break
res*=(endB-startB)+1
print(res)