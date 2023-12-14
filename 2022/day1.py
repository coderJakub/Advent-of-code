from sys import argv

with open(argv[1]) as f:
    content = f.read()

content = content.split("\n\n")
elfs = []
for i,elf in enumerate(content):
    elfs.append(0)
    for eat in elf.split("\n"):
        elfs[i] += int(eat)

elfs.sort()
elfs.reverse()
res=0
for i in range(3):
    res+=elfs[i]
    if i==0:
        print(res)
print(res)