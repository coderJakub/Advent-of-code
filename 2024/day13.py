import heapq

with open('in.txt') as f:
    content = f.read()

# Da nur Gleichungsysteme mit genau einer Lösung gegeben sind, wird nur überprüft, ob die Lösung ganzzahlig und positiv ist
def solve(A,B,E):
    x1, y1 = A
    x2, y2 = B
    e1, e2 = E
    
    t2 = (e2*x1 - e1*y1) / (-x2*y1 + y2*x1)
    t1 = (e1 - t2*x2) / x1
    
    if t1<0 or t2<0 or t1%1!=0 or t2%1!=0:
        return 0
    else:
        return int(t1)*3+int(t2)*1

for p,add in [('1',0), ('2',10000000000000)]:
    ans = 0
    for machine in content.split('\n\n'):
        a,b,end = machine.split('\n')
        a = [int(x[2:]) for x in a.split(': ')[1].split(', ')]
        b = [int(x[2:]) for x in b.split(': ')[1].split(', ')]
        end = [int(x[2:])+add for x in end.split(': ')[1].split(', ')]
        ans += solve(a,b,end)
    
    print(f'Part {p}: {ans}')