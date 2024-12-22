from collections import defaultdict
with open('in.txt') as f:
    content = [int(x) for x in f.read().splitlines()]

prizes = [[x] for x in content]
prizesE = [[] for _ in range(len(content))]
for _ in range(2000):
    for i,num in enumerate(content):
        num = ((num*64)^num)%16777216
        num = ((num//32)^num)%16777216
        num = ((num*2048)^num)%16777216

        prize = int(str(num)[-1])
        content[i] = num
        prizes[i].append(prize)
        prizesE[i].append(prizes[i][-1]-prizes[i][-2])

for i in range(len(prizes)):
    prizes[i].pop(0)

print(f'Part 1: {sum(content)}')

def getScore(prizeE,prize):
    score = {}
    for i in range(len(prizeE)-3):
        d1 = prizeE[i]
        d2 = prizeE[i+1]
        d3 = prizeE[i+2]
        d4 = prizeE[i+3]
        if (d1,d2,d3,d4) in score:
            continue
        score[(d1,d2,d3,d4)] = prize[i+3]
    return score        

ANS = defaultdict(int)
for i in range(len(prizesE)):
    scores = getScore(prizesE[i],prizes[i])
    for k,v in scores.items():
        ANS[k] += v

print(f'Part 2: {max(ANS.values())}')