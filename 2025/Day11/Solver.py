import sys


filename = "in.txt" if len(sys.argv)<1 else sys.argv[1]
with open(filename) as f:
    content = {k: v.split() for line in f.read().splitlines() for (k, v) in (line.split(": "),) }

def dfs(state, seen, found={}):
    key = tuple([state] + sorted(found.items()))
    if key in seen:
        return seen[key]

    if state == 'out' and all(found.values()):
        return 1

    found = {key: val or key == state for key, val in found.items()}

    res = sum(dfs(n, seen, found) for n in content.get(state, []))

    seen[key] = res
    return res


print("Part 1:", dfs("you", {}))
print("Part 2:", dfs("svr", {}, {'fft': False, 'dac': False}))