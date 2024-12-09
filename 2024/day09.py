with open('in.txt') as f:
    lines = f.read()

disk =[] #[ID,Size]
for i in range(0,len(lines),2):
    if i>0:
        disk.append([-1,int(lines[i-1])])
    disk.append([i//2,int(lines[i])])

def orderPart1(disk: list):
    res = []
    
    #Transferiert die Disk in der richtigen Reihenfolge in res und entfernt freie Plätze
    while disk!=[]:
        num, lenN = disk.pop(0)
        if num!=-1:
            res.append([num,lenN])
        else:
            while lenN>0 and disk!=[]:
                if disk[-1][0] == -1:
                    disk.pop()
                else:
                    num2, lenN2 = disk.pop()
                    
                    # Wenn der Platz für das File nicht reicht, restliches File wieder hinten anhängen
                    if lenN2>lenN:
                        disk.append([num2,lenN2-lenN])
                        
                    res.append([num2,min(lenN2,lenN)])
                    lenN -= min(lenN2,lenN)
    return res

def orderPart2(disk: list):
    #Geht von hinten durch die Disk durch und versucht die Files so weit wie möglich nach vorne zu schieben
    for i in range(len(disk)-1,0,-1):
        if disk[i][0] == -1:
            continue
        size = disk[i][1]
        
        # Geht alle freien Plätze, welche vor dem File liegen durch und schaut ob das File dort reinpasst und schiebt es ggf. nach vorne
        for j in range(0,i):
            if disk[j][0] != -1 or size>disk[j][1]: #-> Entweder belegt oder nicht genug Platz
                continue
            num, size = disk.pop(i)
            _,size2 = disk.pop(j)
            
            # Verschiebe das File nach vorne -> freier Platz an der Stelle des Files
            disk.insert(j,[num,size])
            disk.insert(i,[-1,size])
            
            #Wenn das File den freien Platz nicht komplett ausfüllt, wird der Rest als freier Platz hinter dem File angehängt
            if size2>size:
                disk.insert(j+1,[-1,size2-size])
            break
    return disk

#Berechne checksum
for p, orderedList in [('Part 1',orderPart1(disk.copy())),('Part 2',orderPart2(disk.copy()))]:
    count = 0
    k = 0
    for i,size in orderedList:
        for _ in range(size):
            if i!=-1:
                count += i*k
            k+=1
    print(f'{p}: {count}')