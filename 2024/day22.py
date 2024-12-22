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

best = 0
SEEN = set()
for p in prizesE:
    print("---",prizesE.index(p))
    for i in range(len(p)-3):
        d1 = p[i]
        d2 = p[i+1]
        d3 = p[i+2]
        d4 = p[i+3]
        if (d1,d2,d3,d4) in SEEN:
            continue
        SEEN.add((d1,d2,d3,d4))
        score = 0
        for prize,prizeE in zip(prizes,prizesE):
            for k in range(len(prize)-3):
                if prizeE[k] == d1 and prizeE[k+1] == d2 and prizeE[k+2] == d3 and prizeE[k+3] == d4:
                    score += prize[k+3]
                    break
        if score > best:
            best = score
            print(score)

print(f'Part 1: {sum(content)}')
