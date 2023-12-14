from sys import argv

with open(argv[1]) as f:
    content = f.read().splitlines()

def winner(a,b):
    if shape[a]==shape[b]:
        return 3
    if (shape[a]+1)%3==shape[b]:
        return 6
    else:
        return 0

shape = {'A': 0, 'B': 1, 'C':2, 'X':0 , 'Y':1, 'Z':2}
for part2 in [False, True]:    
    res=0
    for round in content:
        round = round.split(" ")
        if part2:
            res+=shape[round[1]]*3
            for i in ['X','Y','Z']:
                if winner(round[0], i)==shape[round[1]]*3:
                    res+=shape[i]+1
        else:
            res+=shape[round[1]]+1+winner(round[0], round[1])
    print(res)