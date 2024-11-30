with open('in.txt') as f:
    content = f.read().splitlines()

numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

L = len(content)
C = len(content[0])

sol = 0
for i,line in content:
    sol = line

print(sol)