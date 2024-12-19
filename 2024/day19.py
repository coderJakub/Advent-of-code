with open('in.txt') as file:
    content = file.read()
    
towels = content.split('\n\n')[0].split(', ')
musters = content.split('\n\n')[1].splitlines()

p1 = 0
p2 = 0

def possible(muster: str, towels: list, seen: dict):
    if muster in seen:
        return seen[muster]
    possibilities = 0
    if muster == '':
        return 1
    for towel in towels:
        if muster.startswith(towel):
            possibilities += possible(muster[len(towel):], towels, seen)
    seen[muster] = possibilities
    return possibilities

for k,muster in enumerate(musters):
    seen = {}
    p = possible(muster, towels, seen)
    p1 += 1 if p > 0 else 0
    p2 += p
print(p1)
print(p2)