with open('in.txt') as f:
    content = f.read().split("\n")

left = [int(l.split("   ")[0]) for l in content]
right = [int(l.split("   ")[1]) for l in content]

p1 = 0
p2 = 0
right = sorted(right)
left = sorted(left)
for i,line in enumerate(left):
    p1 += abs(left[i]-right[i])
    p2 += line*right.count(line)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')