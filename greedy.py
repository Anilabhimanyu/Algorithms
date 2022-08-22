#greedy approach
nums=[int(x) for x in input().split()]
total=int(input('enter the sum'))
req=[]

while total>0:
  a=(total//max(nums))
  for i in range(a):
    req.append(max(nums))
  total-=a*max(nums)
  nums.remove(max(nums))
print(req)