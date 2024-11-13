from sys import argv

with open(argv[1]) as f:
    content = f.read().splitlines()
    
content.pop(0)
content.pop(0)

def look_in_dir(content):
    # Größe des Ordners auf 0
    size = 0
    dirsA = []
    # Solange man sich im Ordner befindet
    while len(content)>0 and not content[0] == "$ cd ..":
        # Wenn cd -> wird in einen Unterordner gewechselt
        if content[0].startswith("$ cd "):
            # Lösche den cd und ls Befehl
            content.pop(0)
            content.pop(0)
            # Untersuche den Unterordner nach Größe und Anzahl der Dateien
            sizeN, dirs = look_in_dir(content)
            # Füge jegliche Größen der Ordner hinzu
            for dir in dirs:
                dirsA.append(dir)
            # Addiere die Größe und Anzahl der Dateien des Unterordners
            size += sizeN
        # Wenn es sich um eine Datei handelt
        elif not content[0].startswith("dir"):
            # Addiere die Größe der Datei und lösche die Zeile
            size += int(content[0].split(" ")[0])
            content.pop(0)
        # Wenn ein Ordner gefunden wurde -> lösche die Zeile
        else:
            content.pop(0)
    # Der Unterordner wurde vollständig untersucht -> lösche den cd .. Befehl
    if len(content)>0:
        content.pop(0)
        
    dirsA.append(size)
    return size, dirsA
        
size, dirs = look_in_dir(content)

ges_size=0
for dir in dirs:
    if dir<=100000:
        ges_size +=dir
print(f"Part 1: {ges_size}")

unused = 70000000 - size
needed = 30000000 - unused
perfect = 30000000
for dir in dirs:
    if dir-needed > 0 and dir<perfect:
        perfect = dir
print(f"Part 2: {perfect}")