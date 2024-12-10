from sys import argv
import pyperclip as pc
fn = argv[1] if len(argv) > 1 else 'input.txt'
with open(fn) as f:
    content = f.read().splitlines()

def printc(text):
    print(text)
    pc.copy(text)

R = len(content)
C = len(content[0])

def bfs(start,grid,dist):
    q_m = [start]
    for k in range(dist):
        q = q_m.copy()
        q_m = []
        while q:
            i,j = q.pop(0)
            for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#' and (ni,nj) not in q_m:
                    q_m.append((ni,nj))
    return len(q_m)


for i,l in enumerate(content):
    for j,c in enumerate(l):
        if c == 'S':
            content[i] = l[:j] + '.' + l[j+1:]
            p1 = bfs((i,j),content,64)
            break
        
printc(p1)