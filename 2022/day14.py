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

def fill_sand(grid, part2=False):
    while True:
        curr = sand_spawn.copy()
        if grid[sand_spawn[0]+1][sand_spawn[1]] == 'o':
            return grid
        while True:
            try:
                if grid[curr[0]+1][curr[1]] == '.':
                    curr[0] +=1
                    continue
                if grid[curr[0]+1][curr[1]-1] =='.':
                    curr[0] +=1
                    curr[1] -=1
                    if curr[1]-1<0:
                        if not part2:
                            return grid 
                        for i in range(len(grid)-1):
                            grid[i].insert(0,'.')
                        grid[-1].insert(0,'#')
                        sand_spawn[1] +=1
                    continue
                if grid[curr[0]+1][curr[1]+1] == '.':
                    curr[0] +=1
                    curr[1] +=1
                    if curr[1]+1<0:
                        if not part2:
                            return grid 
                        for i in range(len(grid)-1):
                            grid[i].insert(0,'.')
                        grid[-1].insert(0,'#')
                        sand_spawn[1] +=1
                    continue
            except:
                if not part2:
                    return grid
                for i in range(len(grid)-1):
                    grid[i].append('.')
                grid[-1].append('#')
                continue
            grid[curr[0]][curr[1]] = 'o'
            break

gridC = grid.copy()
gridC.append(['.' for _ in range(x_bord[1]-x_bord[0]+1)])
gridC.append(['#' for _ in range(x_bord[1]-x_bord[0]+1)])

for part2 in [False, True]: 
    fill_sand(grid, part2)
    count = 0
    for g in grid:
        count += g.count('o')
    print(f'Part {2 if part2 else 1}: {count}')
    grid = gridC