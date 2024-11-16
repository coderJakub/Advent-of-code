from sys import argv
from copy import deepcopy

class Monkey:
    count=0
    def __init__(self, itemList, op, condition):
        self.itemList = itemList
        self.op = op
        self.condition = condition
    def operation(self, part1, lcm=0):
        self.count+=1
        operator1 = self.itemList[0] if self.op[0]=='old' else int(self.op[0]) 
        operator2 = self.itemList[0] if self.op[2]=='old' else int(self.op[2]) 
        match self.op[1]:
            case '+': new = operator1 + operator2
            case '-': new = operator1 - operator2
            case '*': new = operator1 * operator2
            case '/': new = operator1 / operator2
            case _: exit()
        self.itemList[0] = new//3 if part1 else new%lcm
    def giveItem(self, monkeyList):
        cond = self.itemList[0]%self.condition[0] == 0
        monkeyList[self.condition[1] if cond else self.condition[2]].itemList.append(self.itemList[0])
        self.itemList.pop(0)

with open(argv[1]) as file:
    content = file.read().splitlines()

monekys = []
divs = set()
while not content == []:
    content.pop(0)

    items = [int(item) for item in content.pop(0).split(": ")[1].split(", ")]
    operation = content.pop(0).split("= ")[1].split(" ")
    div = int(content.pop(0).split(" ")[5])
    ifB = int(content.pop(0).split(" ")[9])
    elseB = int(content.pop(0).split(" ")[9])

    divs.add(div)
    try:
        content.pop(0)
    except:
        pass
    monekys.append(Monkey(items, operation, [div,ifB,elseB]))
monekysC = deepcopy(monekys)
lcm = 1
for div in divs:
    lcm *= div

for part1 in [True, False]:
    monekys = deepcopy(monekysC)
    for i in range(20 if part1 else 10000):
        for m in monekys:
            while not m.itemList == []:
                m.operation(part1, lcm)
                m.giveItem(monekys)

    max1 = 0
    max2 = 0
    for m in monekys:
        if m.count > max1:
            max2 = max1
            max1 = m.count
        else:
            max2 = max(max2, m.count)
    print(f'{'Part 1' if part1 else 'Part 2'}: {max1*max2}')