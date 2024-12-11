from sys import argv
from collections import defaultdict
from copy import deepcopy
with open(argv[1]) as f:
    content = f.read().splitlines()

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([x for x in graph[node] if x not in visited])
    return len(visited)
    
k1 = 0
dict = []
comp = set()
for line in content:
    k,l = line.split(": ")
    l = l.split(" ")
    k1 += len(l)
    for s in l:
        dict.append((k,s))
        comp.add(k)
        comp.add(s)
val = len(comp)
for k2 in range(k1):
    conectionRemove1 = dict.pop(k2)
    for k3 in range(k1-1):
        conectionRemove2 = dict.pop(k3)
        for k4 in range(k1-2):
            conectionRemove3 = dict.pop(k4)
            dict2 = defaultdict(list)
            for con in dict:
                dict2[con[0]].append(con[1])
                dict2[con[1]].append(con[0])
            dict.insert(k2, conectionRemove3)
            f = bfs(dict2, k)
            if f != val:
                print(f*(val-f))
                exit()
        dict.insert(k3, conectionRemove2)
    dict.insert(k2, conectionRemove1)
        