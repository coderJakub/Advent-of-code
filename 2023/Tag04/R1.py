from sys import argv

def function(data):
    res=0
    for i, line in enumerate(data):
        line = line.split(": ")[1]
        win_num = line.split("| ")[0].split(" ")
        num = line.split("| ")[1].split(" ")
        
        num[len(num)-1]=num[len(num)-1].split("\n")[0]
        
        win_num=list(filter(lambda x: x != '', win_num))
        num=list(filter(lambda x: x != '', num))
        
        winning_num_mult=0.5
        for c in num:
            if c in win_num:
                winning_num_mult*=2
        res+=int(winning_num_mult)
    return res 

with open(argv[1]) as f:
    lines = f.readlines()
print(function(lines))