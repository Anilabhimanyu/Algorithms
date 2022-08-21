# recursion
nums=[int(x) for x in input().split()]
total=int(input('enter the sum'))
req=[]

def noOfCoins(total,nums,req):
  if total==0:
    return sum(req)
  a=(total//max(nums))
  for i in range(a):
    req.append(max(nums))
  total-=a*max(nums)
  nums.remove(max(nums))
  return noOfCoins(total,nums,req)
noOfCoins(total,nums,req)
