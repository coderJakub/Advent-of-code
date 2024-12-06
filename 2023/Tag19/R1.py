from sys import argv

with open(argv[1]) as f:
    content = f.read()

fp,av = content.split('\n\n')

workflows = {line.split('{')[0]:line[:-1].split('{')[1] for line in fp.splitlines()}

def getNextState(workflow, val):
    for cond in workflow.split(','):
        if ':' not in cond:
            return cond
        c,s = cond.split(':')
        if '>' in c and val[c.split('>')[0]]>int(c.split('>')[1]):
            return s
        elif '<' in c and val[c.split('<')[0]]<int(c.split('<')[1]):
            return s

count=0
for a in av.splitlines():
    state = 'in'
    while state!='A' and state!='R':
        val = {v.split('=')[0]:int(v.split('=')[1]) for v in a[1:-1].split(',')}
        state = getNextState(workflows[state], val)
    if state == 'A':
        count+=sum(val.values())
print(count)