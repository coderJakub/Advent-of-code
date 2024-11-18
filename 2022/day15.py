from sys import argv

with open(argv[1]) as f:
    content = f.read().splitlines()

spices = []
for line in content:
    xs = int(line.split(' ')[2].split('=')[1][:-1])
    ys = int(line.split(' ')[3].split('=')[1][:-1])
    xb = int(line.split(' ')[8].split('=')[1][:-1])
    yb = int(line.split(' ')[9].split('=')[1])
    spices.append([xs, ys, xb, yb])

pos = set()
row = 10
for spice in spices:
    diff = abs(spice[0] - spice[2]) + abs(spice[1] - spice[3])
    diff_row = abs(spice[1]-row)
    in_row = diff-diff_row
    for i in range(spice[0]-in_row, spice[0]+in_row+1):
        pos.add(i)
for spice in spices:
    if spice[3] == row and spice[2] in pos:
        pos.remove(spice[2]) 

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1]+1 < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print(f'Part 1: {len(pos)}')
size = 4000000
for row in range(size):
    invs_row = []
    for spice in spices:
        diff = abs(spice[0] - spice[2]) + abs(spice[1] - spice[3])
        diff_row = abs(spice[1]-row)
        in_row = diff-diff_row
        if in_row < 0:
            continue
        inv = [max(0,spice[0]-in_row), min(size,spice[0]+in_row)]
        invs_row.append(inv)
    if not merge_intervals(invs_row) == [[0, size]]:
        break
    
print(f'Part 2: {row+(merge_intervals(invs_row)[1][0]-1)*4000000}')