from collections import defaultdict
import time
with open('in.txt') as f:
    content = f.read().splitlines()

R=103
C=101

for kS in range(1000):
    k=kS*100+22+kS
    endPos = defaultdict(int)
    for line in content:
        pos, v = line.split(' ')
        x,y = [int(x) for x in pos[2:].split(',')]
        xx,yy = [int(x) for x in v[2:].split(',')]
        x,y = (x+xx*k)%C, (y+yy*k)%R
        endPos[(x,y)] += 1
    '''
    q = [0,0,0,0]
    for (x,y),v in endPos.items():
        if x<C//2 and y<R//2:
            q[0] += v
        elif x>C//2 and y>R//2:
            q[3] += v
        elif x<C//2 and y>R//2:
            q[2] += v
        elif x>C//2 and y<R//2:
            q[1] += v

    print(q[0]*q[1]*q[2]*q[3])
    '''
    print()
    for i in range(R):
        for j in range(C):
            if endPos[(j,i)] > 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print(k)
    time.sleep(0.5)