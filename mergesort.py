def merge_sort(nums):
  if len(nums)<=1:
    return nums
  mid=(0+len(nums))//2
  left_set=merge_sort(nums[:mid])
  right_set=merge_sort(nums[mid:])
  sorted_nums=merge(left_set,right_set)
  return sorted_nums
def merge(list_l,list_r):
  '''
  len_list_l=len(left_l)
  len_list_r=len(list_r)
  for i in range(len_list_l):
    for j in range(len_list_r):
      if list_l(i)>list()'''
  sorted_list=[]
  i,j=0,0
  while i<len(list_l) and j<len(list_r):
    if list_l[i]<list_r[j]:
      sorted_list.append(list_l[i])
      i+=1
    else:
      sorted_list.append(list_r[j])
      j+=1
  return sorted_list
merge_sort([4,2,7,5,4,2])