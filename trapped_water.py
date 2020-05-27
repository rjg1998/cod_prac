# -*- coding: utf-8 -*-
"""Trapped_water.ipynb

def water_capacity(arr):
  max_index=arr.index(max(arr))   # find the index of maximum number in array
  capacity=0         
  sum=0
  size=0
 
  for i in range(max_index+1):    # finding water capacity before max index
    if size>arr[i]:
      sum+=size-arr[i]              
    else: 
      capacity+=sum
      sum=0
      size=arr[i]
  size=0
  for j in range(len(arr)-1,max_index-1,-1): # finding water capacity after max index
    if size>arr[j]:
      sum+=size-arr[j]
    else: 
      capacity+=sum
      sum=0
      size=arr[j]
  return capacity

a=[1,0,2,0,1,4,2,4,1,3,0,3]
print(water_capacity(a)) # prints 11
b=range(10,-1,-1)
print(water_capacity(b)) # prints 0


