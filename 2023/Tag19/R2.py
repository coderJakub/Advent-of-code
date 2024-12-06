from sys import argv

with open(argv[1]) as f:
    content = f.read()

fp = content.split('\n\n')[0]

workflows = {line.split('{')[0]:line[:-1].split('{')[1] for line in fp.splitlines()}

def interval_intersection(a, b):
    result = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])

        if start <= end:
            result.append([start, end])

        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1

    return result
def interval_union(a, b):
    intervals = sorted(a + b, key=lambda x: x[0])
    result = []

    for interval in intervals:
        if not result or result[-1][1] < interval[0] - 1:
            result.append(interval)  # Füge das Intervall direkt hinzu
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result

def intersect(a,b):
    for k in a:
        a[k] = interval_intersection(a[k],b[k])
    return a

def union(a,b):
    for k in a:
        a[k] = interval_union(a[k],b[k])
    return a

def getPossib(p_org,s):
    p_res = {'a':[], 'm':[], 'x':[], 's':[]}
    for wf in workflows:
        p = p_org.copy()
        v=workflows[wf]
        if s not in v:
            continue
        if wf!='in':
            p=intersect(getPossib(p,wf),p)
        for cond_n in v.split(',')[:-1]:
            cond,n = cond_n.split(':')
            inti = {'a':[[0,4000]], 'm':[[0,4000]], 'x':[[0,4000]], 's':[[0,4000]]}
            if n==s:
                if '>' in cond:
                    inti[cond.split('>')[0]][0][0] = int(cond.split('>')[1])+1
                elif '<' in cond:
                    inti[cond.split('<')[0]][0][1] = int(cond.split('<')[1])-1
                p = intersect(p,inti)
                break
            if '>' in cond:
                inti[cond.split('>')[0]][0][1] = int(cond.split('>')[1])-1
            elif '<' in cond:
                inti[cond.split('<')[0]][0][0] = int(cond.split('<')[1])+1
            p = intersect(p,inti)
        p_res = union(p_res,p)
        print(s,p)
    return p_res

possib_v = {'x':[[1,4000]], 'm':[[1,4000]], 'a':[[1,4000]], 's':[[1,4000]]}
print(getPossib(possib_v,'A'))
print(4000*4000*4000*((1350)+(2769-1352)+(3447-2771)+(3449-4000)))
print(167409079868000)