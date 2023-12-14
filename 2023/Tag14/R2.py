from sys import argv

with open(argv[1]) as f:
    content=f.read().splitlines()
content = [list(i) for i in content]
def cycle(l): 
    for row,dataR in enumerate(content):
        for col,dataC in enumerate(dataR):
            if row==0:
                break
            if dataC=='O':
                i=row-1
                while i>=0:
                    if content[i][col] in ['#', 'O']:
                        break
                    i-=1
                i+=1
                content[row][col] = '.'
                content[i][col] = 'O'
    for col in range(len(content[0])):
        for row,dataR in enumerate(content):
            if col==0:
                break
            if dataR[col]=='O':
                i=col-1
                while i>=0:
                    if content[row][i] in ['#', 'O']:
                        break
                    i-=1
                i+=1
                content[row][col] = '.'
                content[row][i] = 'O'
    content.reverse()
    for i in range(len(content)):
        content[i].reverse()
    if l==0:
        cycle(1)
        
for i in range(3):
    print(i)
    cycle(0)

for i in content:
    print(i)