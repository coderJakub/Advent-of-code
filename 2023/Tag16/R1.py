from sys import argv
with open(argv[1]) as f:
    content = f.read().splitlines()
    
field = [[0 for i in range(len(content[j]))]for j in range(len(content))]

def drawWayBeam(beam):
    curr=beam[0]
    direction=beam[1]
    while True:
        if curr[0]<0 or curr[1]<0 or curr[0]>=len(content) or curr[1]>=len(content[0]) or field[curr[0]][curr[1]]==(direction):
            (curr)
            break
        field[curr[0]][curr[1]]=direction
        if content[curr[0]][curr[1]]=='/':
            if direction==[1,0]:
                direction=[0,-1]
            elif direction==[0,1]:
                direction=[-1,0]
            elif direction==[-1,0]:
                direction=[0,1]
            elif direction==[0,-1]:
                direction=[1,0]
        if content[curr[0]][curr[1]]=='\\':
            if direction==[1,0]:
                direction=[0,1]
            elif direction==[0,1]:
                direction=[1,0]
            elif direction==[-1,0]:
                direction=[0,-1]
            elif direction==[0,-1]:
                direction=[-1,0]
        if content[curr[0]][curr[1]]=='-':
            if direction in [[1,0],[-1,0]]:
                beams.append([curr,[0,1]])
                direction=[0,-1]
        if content[curr[0]][curr[1]]=='|':
            if direction in [[0,1],[0,-1]]:
                beams.append([curr,[1,0]])
                direction=[-1,0]
        curr=[curr[0]+direction[0],curr[1]+direction[1]]

beams=[[[0,0],[0,1]]]
while len(beams)!=0:
    drawWayBeam(beams[0])
    beams.pop(0)

res=0    
for i in field:
    for j in i:
        if j != 0:
            res+=1
print(res)