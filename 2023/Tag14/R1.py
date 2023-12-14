from sys import argv

with open(argv[1]) as f:
    content=f.read().splitlines()

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
            content[row]=content[row][:col] + '.' + content[row][col + 1:]
            content[i]=content[i][:col] + 'O' + content[i][col + 1:]
load=0
for row,dataR in enumerate(content):
    load+=dataR.count("O")*(len(content)-row)
print(load)