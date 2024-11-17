from sys import argv

with open(argv[1]) as f:
    content = f.read().splitlines()

x = []
y = []
for line in content:
    x.append([int(point.split(',')[0]) for point in line.split(' -> ')])
    y.append([int(point.split(',')[1]) for point in line.split(' -> ')])

x_bord = [min([min(i) for i in x]), max([max(i) for i in x])]
y_bord = [min([min(i) for i in y]), max([max(i) for i in y])]

x_norm = [[i-x_bord[0] for i in p] for p in x]

grid = [['.' for _ in range(x_bord[1]-x_bord[0]+1)] for _ in range(y_bord[1]+1)]

for l, x_l in enumerate(x_norm):
    y_l = y[l]
    for k in range(1,len(x_l)):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i<=max(y_l[k],y_l[k-1]) and i>=min(y_l[k],y_l[k-1]) and j<=max(x_l[k],x_l[k-1]) and j>=min(x_l[k],x_l[k-1]):
                    grid[i][j] = '#' 

sand_spawn = [-1, 500-x_bord[0]]

def fill_sand(grid):
    while True:
        curr = sand_spawn.copy()
        while True:
            try:
                if grid[curr[0]+1][curr[1]] == '.':
                    curr[0] +=1
                    continue
                if grid[curr[0]+1][curr[1]-1] =='.':
                    curr[0] +=1
                    curr[1] -=1
                    continue
                if grid[curr[0]+1][curr[1]+1] == '.':
                    curr[0] +=1
                    curr[1] +=1
                    continue
            except:
                return grid
            grid[curr[0]][curr[1]] = 'o'
            break

fill_sand(grid)
for g in grid:
    print(g)
exit()
count = 0
for g in grid:
    count += g.count('o')
print(count)