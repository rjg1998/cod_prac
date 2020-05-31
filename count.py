# -*- coding: utf-8 -*-
"""count.ipynb


count=0
def quick_sort(arr,l,r,count):
  if l==r or l>r:
    return arr , count
  else:
    
    pivot=arr[r]
    index=l
    for i in range(l,r):
      if arr[i]<pivot:
        if arr[index]!=arr[i]:
          count+=1
          arr[index],arr[i]=arr[i],arr[index]
          print(count,arr)
        index+=1
          
    if arr[index]!=pivot:
      arr[index],arr[r] = arr[r] , arr[index]
      count+=1
      print(count,arr)
    arr,count=quick_sort(arr,l,index-1,count)
    arr,count=quick_sort(arr,index+1,r,count)
    return arr , count

quick_sort([2,3,41,9,4,10,21],0,6,count)

b=[2,3,9,4,10]
quick_sort(b,0,4,0)

def selection_sort(arr):
  count=0
  for i in range(len(arr)):
    index=arr.index(min(arr[i:]))
    if i!=index:
      arr[i],arr[index]=arr[index],arr[i]
      count+=1
  return arr, count

selection_sort([2,3,41,9,4,10,21])

