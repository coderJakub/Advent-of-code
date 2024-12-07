import itertools
with open('in.txt') as f:
    content = f.read().splitlines()

p1 = 0
p2 = 0
print("Takes around 40 seconds to run")
for k,line in enumerate(content):
    str_result, str_z = line.split(': ')
    nums = [int(x) for x in str_z.split(' ')]
    r = int(str_result)
    part2 = False
    for iter in list(itertools.product(["*","+", '|'], repeat=len(nums)-1)):
        result = nums[0]
        for n in range(len(nums[:-1])):
            match iter[n]:
                case '+':
                    result += nums[n+1]
                case '*':
                    result *= nums[n+1]
                case '|':
                    result = int(str(result) + str(nums[n+1]))
        if result == r and iter.count('|') != 0:
            p2 += r
            part2 = True
        elif result == r:
            p1 += r
            if not part2:
                p2 += r
            break
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')