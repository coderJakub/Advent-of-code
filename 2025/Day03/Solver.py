import sys

filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = [list(map(int, list(line))) for line in f.read().splitlines()]
    
res = [0,0]

for line in content:
    for part, am in enumerate([2, 12]):
        nums = []
        start = 0
        for k in range(am)[::-1]:
            digit = max(line[start:len(line)-k])
            nums.append(str(digit))
            start += line[start:len(line)-k].index(digit) + 1
        res[part] += int("".join(nums))

print(f"Part 1: {res[0]}")
print(f"Part 1: {res[1]}")