from sys import argv

class Monkey:
    count=0
    def __init__(self, itemList, op, condition):
        self.itemList = itemList
        self.op = op
        self.condition = condition
    def operation(self, part1):
        self.count+=1
        operator1 = self.itemList[0] if self.op[0]=='old' else int(self.op[0]) 
        operator2 = self.itemList[0] if self.op[2]=='old' else int(self.op[2]) 
        match self.op[1]:
            case '+': new = operator1 + operator2
            case '-': new = operator1 - operator2
            case '*': new = operator1 * operator2
            case '/': new = operator1 / operator2
            case _: exit()
        self.itemList[0] = int(new/3) if part1 else new
    def giveItem(self, monkeyList):
        cond = self.itemList[0]%self.condition[0] == 0
        monkeyList[self.condition[1] if cond else self.condition[2]].itemList.append(self.itemList[0])
        self.itemList.pop(0)
    def printS(self):
        print(f'Items: {self.itemList}, Op: {self.op}, Condition: {self.condition}, C {self.count}')

with open(argv[1]) as file:
    content = file.read().splitlines()

part1 = argv[2]=='part1'
monekys = []
while not content == []:
    content.pop(0)

    items = [int(item) for item in content.pop(0).split(": ")[1].split(", ")]
    operation = content.pop(0).split("= ")[1].split(" ")
    div = int(content.pop(0).split(" ")[5])
    ifB = int(content.pop(0).split(" ")[9])
    elseB = int(content.pop(0).split(" ")[9])

    try:
        content.pop(0)
    except:
        pass
    monekys.append(Monkey(items, operation, [div,ifB,elseB]))

for i in range(20 if part1 else 18):
    for m in monekys:
        while not m.itemList == []:
            m.operation(part1)
            m.giveItem(monekys)
        
for m in monekys:
    m.printS()
max1 = 0
max2 = 0
for m in monekys:
    if m.count > max1:
        max2 = max1
        max1 = m.count
print(f'{'Part 1' if part1 else 'Part2'}: {max1*max2}')