from sys import argv
with open(argv[1]) as f:
    content = f.read().splitlines()

class FlipFlop:
    def __init__(self, follows,name):
        self.name = name
        self.follows = follows  
        self.state = False
    def execute(self,pulse,pre):
        if pulse == 'h':
            return []
        if self.state:
            self.state = False
            return [(i,'l',self.name)for i in self.follows]
        self.state = True
        return [(i,'h',self.name) for i in self.follows]
    def __str__(self):
        return f'FlipFlop {self.name=} {self.follows=} {self.state=}'

class Conjuction:
    def __init__(self, follows,store,name):
        self.name = name
        self.follows = follows
        self.store = store
    def execute(self,pulse,pre):
        self.store[pre] = pulse
        if all(i == 'h' for i in self.store.values()):
            return [(i,'l',self.name) for i in self.follows]
        return [(i,'h',self.name) for i in self.follows]   
    def __str__(self):
        return f'Conjuction {self.name=} {self.follows=} {self.store=}'     


parts = {}
for line in content:
    name,follows = line.split(' -> ')
    follows = follows.split(', ')
    if name == 'broadcaster':
        start = follows
    elif name.startswith('%'):
        name = name[1:]
        parts[name] = FlipFlop(follows,name)
    else:
        name = name[1:]
        pre = []
        for line in content:
            if line.count(name)>0 and not line[1:].startswith(name):
                pre.append(line[1:].split(' -> ')[0])
        parts[name] = Conjuction(follows,{i:'l' for i in pre},name)

queue = []
l=0
h=0
for _ in range(1000):
    l+=1
    for i in start:
        queue.append((i,'l','broadcaster'))

    while queue:
        name,pulse,pre = queue.pop(0)
        if pulse == 'h':
            h+=1
        else:
            l+=1
        if name not in parts:
            continue
        test = parts[name].execute(pulse,pre)
        for i in test:
            queue.append(i)
print(l*h)