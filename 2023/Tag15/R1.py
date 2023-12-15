from sys import argv

with open(argv[1]) as f:
    content = f.read()

def hashFunc(string):
    return ((ord(string[-1])+hashFunc(string[:-1]))*17)%256 if len(string)!=1 else (ord(string[0])*17)%256

res = 0
for string in content.split(","):
    res+=hashFunc(string)
print(res)