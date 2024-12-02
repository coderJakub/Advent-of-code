with open('in.txt') as f:
    lines = f.read().splitlines()

grid = [[int(c) for c in line.split(' ')]for line in lines]

def isSafe(line):
    decrease = False if line[0] < line[1] else True
    for k,i in enumerate(line[:-1]):
        if abs(i - line[k+1])>3 or abs(i - line[k+1])==0 or (decrease and i < line[k+1]) or (not decrease and i > line[k+1]):
            return (False,k)
    return (True,0)

unsafe_p1 = 0
unsafe_p2 = 0
for line in grid:
    safe,k = isSafe(line)
    if not safe:
        unsafe_p1 += 1
        if not isSafe(line[:k] + line[k+1:])[0] and not isSafe(line[:k+1] + line[k+2:])[0]:
            unsafe_p2 += 1   

print(f'Part 1: {len(grid) - unsafe_p1}')
print(f'Part 2: {len(grid) - unsafe_p2}')