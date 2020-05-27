# -*- coding: utf-8 -*-
"""infinite_array.ipynb


### Assumption array is very large as compared to the index of required number

def binary_search(arr,l,r,num):  #"simple binary search code"
    mid=int((l+r)/2)
    if arr[mid]==num:
        return mid
    elif arr[mid]>num:
        return binary_search(arr,l,mid,num)
    else: return binary_search(arr,mid,r,num)

def infinite_array(arr,num):   # code to find num in an infinite array
    i=0
    while num > arr[2**i] :       # if num to find is greater than number at index 2 power i we increase i by one
        i+=1
    if a[2**i]==num:              # num to find equals number at index 2 power i
        return 2**i
    else: return binary_search(arr,2**(i-1),2**i,num)  # num to find is less than number at index 2 pow i and greater than num at index 2 pow (i-1)
                                                       # then apply binary search between index 2 pow i and 2 pow (i-1)

a=range(300000)

print(infinite_array(a,32))   # returns 32
print(infinite_array(a,31))   # returns 31
print(infinite_array(a,33))     # returns 33
print(infinite_array(a,10000))     # returns 10000
print(infinite_array(a,100000))     # returns 100000

print(infinite_array(a,32))

