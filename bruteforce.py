#brute force
nums=sorted([int(x) for x in input().split()])     # 1,2,5
total=int(input('enter the sum'))                  # 15
req=[]
count=1
i=0
while total>=0:
    if total-nums[i]>=0:
        req.append(nums[i])
        total=total-nums[i]
        print('total-----------',total)
        i+=1
        count+=1
        if count>len(nums):
            i=0
            count=1
    else:
        i=0
        count=1
    
print(req)