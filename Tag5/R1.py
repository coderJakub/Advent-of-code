from sys import argv

def converter(nums,i,converts):
    convertPossibs = converts.split("\n")
    #print(i,": ",convertPossibs,nums)
    print(i, ":", convertPossibs)
    for j,num in enumerate(nums):
        for k,convert in enumerate(convertPossibs):
            if int(num)>=int(convert.split(" ")[1]) and int(num)<int(convert.split(" ")[1])+int(convert.split(" ")[2]):
                nums[j]=int(convert.split(" ")[0])+int(num)-int(convert.split(" ")[1])
    return nums

f = open(argv[1])
content = f.read()
converts = content.split("\n\n")
for i in range(1,len(converts)):
    converts[i]=converts[i].split(":\n")[1]
converts[0] = converts[0].split(": ")[1]

nums=converts[0].split(" ")
for i,convert in enumerate(converts):
    if i!=0:
        nums=converter(nums,i,convert)
lowest=int(nums[0])
print(nums)
for n in nums:
    if int(n)<lowest:
        lowest=n
print(lowest)