import re
with open('in.txt') as f:
    content = f.read()
    

def mul(s):
    nums = s[4:-1].split(',')
    return int(nums[0]) * int(nums[1])

# Verkürzte Lösung mit regulären Ausdrücken
reg = re.compile(r'mul\(\d{0,3},\d{0,3}\)')
print(f'Part 1: {sum([mul(x) for x in reg.findall(content)])}')

enabled = True
s = ""
for i in range(len(content)):
    if content[i:].startswith('do()'):
        i+=3
        enabled = True
    elif content[i:].startswith("don't()"):
        i+=4
        enabled = False
    if enabled:
        s += content[i]
print(f'Part 2: {sum([mul(x) for x in reg.findall(s)])}')
    
# Eigentliche Lösung
'''for part in [1, 2]:
    sum = 0
    enabled = True
    lines = content
    while lines != '':
        if lines[:4] == 'do()':
            enabled = True
            lines = lines[4:]
            continue
        elif lines[:7] == "don't()":
            enabled = False
            lines = lines[7:]
            continue
        elif lines[:4] == 'mul(' and lines[4] in '0123456789':
            correct = True
            i = 4
            while lines[i] != ',':
                if lines[i] not in '0123456789':
                    correct = False
                    break
                i += 1
            i+=1
            while lines[i] != ')':
                if lines[i] not in '0123456789':
                    correct = False
                    break
                i += 1 
            if correct:
                sum += mul(lines[:i+1]) if part==1 or enabled else 0
                lines = lines[i+1:]
                continue
        lines = lines[1:]
    print(f'Part {part}: {sum}')
'''        