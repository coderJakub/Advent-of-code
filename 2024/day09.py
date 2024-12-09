with open('in.txt') as f:
    lines = f.read()

disk =[]
id = 0
for i in range(0,len(lines),2):
    if i>0:
        disk.append([-1,int(lines[i-1])])
    disk.append([id,int(lines[i])])
    id +=1

p1 = disk.copy()
p2 = disk.copy()        

#-----------------Part 1-----------------
count = 0
k=0
while p1!=[]:
    num, lenN = p1.pop(0)
    if num!=-1:
        for i in range(lenN):
            count += num*k
            k+=1
    else:
        while lenN>0 and p1!=[]:
            if p1[-1][0] == -1:
                p1.pop()
            else:
                num2, lenN2 = p1.pop()
                if lenN2>lenN:
                    p1.append([num2,lenN2-lenN])
                lenN2 = min(lenN2,lenN)
                for i in range(lenN2):
                    count += num2*k
                    k+=1
                lenN -= lenN2
print(f'Part 1: {count}')


#-----------------Part 2-----------------
for i in range(len(p2)-1,0,-1):
    if p2[i][0] == -1:
        continue
    size = p2[i][1]
    for j in range(0,i):
        if p2[j][0] != -1 or size>p2[j][1]:
            continue
        num, size = p2.pop(i)
        _,size2 = p2.pop(j)
        p2.insert(j,[num,size])
        p2.insert(i,[-1,size])
        if size2>size:
            p2.insert(j+1,[-1,size2-size])
        break
k=0
count = 0
for i,size in p2:
    for _ in range(size):
        if i!=-1:
            count += i*k
        k+=1
print(f'Part 2: {count}')