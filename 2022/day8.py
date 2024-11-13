from sys import argv

with open(argv[1]) as f:
    content = [list(line) for line in f.read().splitlines()]
    
count = 0
scores = [[0 for i in content[0]] for j in content]
for i in range(len(content)):
    for j in range(len(content[i])):
        curr = content[i][j]
        if j == 0 or i == 0 or i == len(content)-1 or j == len(content[i])-1:
            scores[i][j] = 0
            count += 1
            continue
        # Look how many trees are visible from top
        scoreT = 0
        for k in range(i-1, -1, -1):
            if content[k][j] >= curr:
                scoreT = i-k
                break
        
        # Bottom
        scoreB = 0
        for k in range(i+1, len(content)):
            if content[k][j] >= curr:
                scoreB = k-i
                break
        
        # Left
        scoreL = 0
        for k in range(j-1, -1, -1):
            if content[i][k] >= curr:
                scoreL = j-k
                break
        
        # Right
        scoreR = 0
        for k in range(j+1, len(content[i])):
            if content[i][k] >= curr:
                scoreR = k-j
                break
            
        scores[i][j] = i if scoreT==0 else scoreT
        scores[i][j] *= len(content)-i-1 if scoreB==0 else scoreB
        scores[i][j] *= j if scoreL==0 else scoreL
        scores[i][j] *= len(content[i])-j-1 if scoreR==0 else scoreR
        
        if scoreT==0 or scoreB==0 or scoreL==0 or scoreR==0:
            count += 1
        
max_score = 0
for i in range(len(scores)):
    for j in range(len(scores[i])):
        if scores[i][j] > max_score:
            max_score = scores[i][j]
        
print(f"Part 1: {count}")
print(f"Part 2: {max_score}")            