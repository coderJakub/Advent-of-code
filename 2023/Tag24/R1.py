from sys import argv
import numpy as np
with open(argv[1]) as f:
    content = f.read().splitlines()

vector = []   
for line in content:
    g = line.split(' @ ')[0].split(', ')[:-1]
    g = [int(x) for x in g]
    r = line.split(' @ ')[1].split(', ')[:-1]
    r = [int(x) for x in r]
    vector.append((g, r))

def calculate_intersection(g1, g2):
    p1,r1 = g1
    p2,r2 = g2
    p1, r1, p2, r2 = map(np.array, (p1, r1, p2, r2))

    A = np.column_stack((r1, -r2))
    b = p2 - p1
    
    try:
        t = np.linalg.solve(A, b)
        t1, t2 = t
        intersection_point = p1 + t1 * r1

        return intersection_point,(t1,t2)
    except np.linalg.LinAlgError:
        return None

p1 = 0
testarea = [200000000000000,400000000000000]
for i, vec1 in enumerate(vector):
    for j, vec2 in enumerate(vector[i+1:]):
        t = calculate_intersection(vec1, vec2)
        if t is None:
            continue
        (x,y), (t1,t2) = t
        if testarea[0]<=x<=testarea[1] and testarea[0]<=y<=testarea[1] and t1>=0 and t2>=0:
            p1 += 1       
print(p1)