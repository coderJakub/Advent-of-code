from sys import argv

with open(argv[1]) as file:
    instructions = [line for line in file.read().splitlines()]
x = 1
count = 0
cycle = 0
grid = []
num = -1

def doCycle():
    global x, count, cycle, grid, num
    if cycle%40 == 0:
        grid.append([])
        num+=1
    if cycle%40<=x+1 and cycle%40>=x-1:
        grid[num].append('#')
    else:
        grid[num].append('.')
    cycle += 1
    if ((cycle - 20)%40) == 0:
        count += x*cycle
        
for line in instructions:
    doCycle()
    if line.startswith('noop'):
        continue
    doCycle()
    x += int(line.split()[1])

print(f'Part 1: {count}')
print('Part 2: ')
for line in grid:
    print(line)