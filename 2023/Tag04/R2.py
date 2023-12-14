from sys import argv

def getValue(data):
    res=0
    l = [1]*len(data)
    for i, line in enumerate(data):
        line = line.split(": ")[1]
        win_num = line.split("| ")[0].split(" ")
        num = line.split("| ")[1].split(" ")
        
        num[len(num)-1]=num[len(num)-1].split("\n")[0]
        
        win_num=list(filter(lambda x: x != '', win_num))
        num=list(filter(lambda x: x != '', num))
        k=i+1
        for c in num:
            if c in win_num:
                if k<len(l)-1:
                    l[k]+=l[i]
                else:
                    l.append(l[i])
                k+=1
    for i in range(0,len(l)):
        res+=l[i]
    return res 


with open(argv[1]) as f:
    lines = f.readlines()
print(getValue(lines))