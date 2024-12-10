from collections import defaultdict
with open('in.txt') as file:
    content = file.read().splitlines()
    
R = len(content)
C = len(content[0])

p1 = 0
p2 = 0

trailhead = []
for i,row in enumerate(content):
    for j,c in enumerate(row):
        if c == '0':
            trailhead.append((i,j))
            
def bfs(start, grid, part2=False):
    q = [start] 
    visited = set()
    nines_found = 0
    while q:
        i,j= q.pop(0)
        if (i,j) in visited and not part2:
            continue
        visited.add((i,j))
        if grid[i][j] == '9':
            nines_found += 1
            continue
        for ii,jj in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
            if 0 <= ii < R and 0 <= jj < C and grid[ii][jj] != '.' and int(grid[i][j])+1==int(grid[ii][jj]):
                q.append((ii,jj))
        
    return nines_found

for start in trailhead:
    p1 += bfs(start,content)   
    p2 += bfs(start,content,True) 


print(p1)
print(p2)