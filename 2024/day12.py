with open('in.txt') as f:
    content = f.read().splitlines()
    
R = len(content)
C = len(content[0])
p1 = 0
p2 = 0
visited = set()
for i,line in enumerate(content):
    for j,c in enumerate(line):
        if (i,j) in visited:
            continue
        q = [(i,j)]
        visited.add((i,j))
        sides = []
        area = 0
        while q:
            area +=1
            x,y = q.pop(0)
            for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0 <= nx < R and 0 <= ny < C and content[nx][ny] == c:
                    if (nx,ny) in visited:
                        continue
                    q.append((nx,ny))
                    visited.add((nx,ny))
                else:
                    sides.append((nx,ny,x-nx,y-ny))
        p1 += len(sides)*area
        
        sidesN = 0
        while sides:
            sidesN += 1
            x,y,xx,yy = sides.pop(0)
            q = [(x,y,xx,yy)]
            while q:
                x,y,xx,yy = q.pop(0)
                for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (nx,ny,xx,yy) in sides:
                        sides.remove((nx,ny,xx,yy))
                        q.append((nx,ny,xx,yy))                        
        p2 += sidesN*area

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')