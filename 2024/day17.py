with open('in.txt') as f:
    content = f.read()
    
register = [int(x.split(': ')[1]) for x in content.split('\n\n')[0].splitlines()]
instructions = [int(x) for x in content.split('\n\n')[1].split(': ')[1].split(',')]
instrVal = []
for i in range(0,len(instructions),2):
    instrVal.append((instructions[i],instructions[i+1]))
    
def comboVal(x,register):
    if x<4: return x
    return register[x-4]

def run(instructions, register):
    ip = 0
    output = []
    while ip < len(instructions):
        f,x = instructions[ip]
        match f:
            case 0: register[0] = int(register[0]/(2**comboVal(x,register)))
            case 1: register[1] ^= x
            case 2: register[1] = comboVal(x,register)%8
            case 3: ip = x-1 if register[0]!=0 else ip
            case 4: register[1] = register[1]^register[2]
            case 5: output.append(comboVal(x,register)%8)
            case 6: register[1] = int(register[0]/(2**comboVal(x,register)))
            case 7: register[2] = int(register[0]/(2**comboVal(x,register)))
        ip += 1
    return output

print(f"Part 1: {','.join(map(str,run(instrVal, register)))}")

#Nach Analyse des Codes ist zu erkennen dass A immer durch 8 ganzzahlig dividiert wird und alle Schritte solange wiederholt werden bis A=0 dabei wird immer nur ein Wert ausgegeben
#Daher lassen sich von hinten nach vorne die Werte von A berechnen, indem man immer den Wert von A mit 8 multipliziert und dann überprüft ob die Ausgabe in den nächsten 8 Zahlen nach A die nächste Instruktion ist

def findNumber(i,aBefore,nums):
    if nums == []:
        return aBefore
    for sA in range(max(8**i,aBefore*8),aBefore*8+8):
        register = [sA,0,0]
        if run(instrVal[:-1], register)[0] == nums[0]:
            res= findNumber(i+1,sA,nums[1:])
            if res != None:
                return res
    return None

print(f"Part 2: {findNumber(0,0,instructions[::-1])}")