from sys import argv
with open(argv[1]) as f:
    content = f.read()

instructions = content.split("\n\n")[1].splitlines()
content = content.split("\n\n")[0].splitlines()
stacks = list(filter(lambda x: x != '', content[-1].split(" ")))
content.reverse()
content.pop(0)

for part2 in [False, True]:
    crates = [[] for _ in range(len(stacks))]
    for i in range(len(stacks)):
        for j in range(len(content)):
            if content[j][i*4]!="[":
                break
            crates[i].append(content[j][i*4+1])
    for i in range(len(instructions)):
        anz=int(instructions[i].split("move ")[1].split(" from")[0])
        to =int(instructions[i].split("to ")[1])-1
        of =int(instructions[i].split("from ")[1].split(" to")[0])-1
        temp=[]
        for j in range(anz):
            if not part2:
                crates[to].append(crates[of].pop(-1))
            else:
                temp.append(crates[of].pop(-1))
        temp.reverse()
        for i in temp:
            if part2:
                crates[to].append(i)
    res=""
    for i in crates:
        res+=i[-1]
    print(res)