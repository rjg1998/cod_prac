# -*- coding: utf-8 -*-

input=[2,4,6,8,10,12,14,16,20]
def miss_ele(arr):
    mid=int(len(arr)/2)
    n=len(arr)
    if n==3:
      return arr[0]+arr[2]-arr[1]
    elif n==2:
      return int((arr[0]+arr[1])/2)
    elif (arr[mid]-arr[0])/(mid)>(arr[n-1]-arr[mid])/(n-mid-1):
      return miss_ele(arr[:mid+1])
    else: return miss_ele(arr[mid:])
miss_ele(input)

