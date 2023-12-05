from sys import argv

def interval_intersection(interval1, interval2):
    start1, range1 = interval1
    start2, range2 = interval2

    end1 = start1 + range1 - 1  # Berechnung des Endpunkts des ersten Intervalls
    end2 = start2 + range2 - 1  # Berechnung des Endpunkts des zweiten Intervalls

    start_intersect = max(start1, start2)
    end_intersect = min(end1, end2)

    if start_intersect <= end_intersect:
        intersect_range = end_intersect - start_intersect+1
        return [[start1,start_intersect-start1],[start_intersect, intersect_range],[start_intersect+intersect_range, end1-start_intersect-intersect_range+1]]
    else:
        return None

def converter(nums,i,converts):
    convertPossibs = converts.split("\n")
    res=[n for n in nums]
    print(i, nums,convertPossibs)
    for j,num in enumerate(nums):
        for k,convert in enumerate(convertPossibs):
            print(j,k,num,convert)
            intersection = interval_intersection([num[0], num[1]], [int(convert.split(" ")[1]),int(convert.split(" ")[2])])
            if intersection!=None:
                print(intersection)
                nums[j]=intersection[1]
                nums[j][0]=int(convert.split(" ")[0])+nums[j][0]-int(convert.split(" ")[1])
                if intersection[0][1]>0:
                    nums.append(intersection[0])
                if intersection[2][1]>0:
                    nums.append(intersection[2])
                break
        print(nums)
    return nums

f = open(argv[1])
content = f.read()
converts = content.split("\n\n")
for i in range(1,len(converts)):
    converts[i]=converts[i].split(":\n")[1]
converts[0] = converts[0].split(": ")[1]

nums=converts[0].split(" ")
numsStart=[int(nums[i*2]) for i in range(int(len(nums)/2))]
numsRange=[int(nums[i*2+1]) for i in range(int(len(nums)/2))]
nums=[[numsStart[i], numsRange[i]]for i in range(len(numsStart))]

for i,convert in enumerate(converts):
    if i!=0:
        nums=converter(nums,i,convert)

lowest=int(nums[0][0])
for n in nums:
    if n[0]<lowest:
        lowest=n[0]
print(lowest)