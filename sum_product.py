# -*- coding: utf-8 -*-
"""sum_product.ipynb



a=[1,1,3]
b=[0,2,3,4,5]
 #"To obtain product of two numbers in array format"
def no_product(a,b):
  while a[0]==0: # removing leading zeros in input no.s
    a=a[1:]
  while b[0]==0:
    b=b[1:]
  n=len(a)
  m=len(b)
  c = [0]*(n+m)    # creating empty ans array
  for i in range(n):
    for j in range(m):
      c[n+m-1-i-j]+=a[n-1-i]*b[m-1-j]   
      if c[n+m-1-i-j]>9:
        c[n+m-1-i-j] = c[n+m-1-i-j]%10
        c[n+m-2-i-j] = c[n+m-1-i-j]//10+c[n+m-2-i-j]
  if c[0]==0:
    c=c[1:]
  return c
no_product(a,b)

# "To add two no.s in array format"
def no_add(a):  
  while a[0]==0:   # removing leading zeros in input no
    a=a[1:]
  n=len(a)-1 
  bol=True 
  while n!=-1:     # adding 1 to last digit
    a[n]+=1
    if a[n]>9:        # if the digit is 9 in which 1 is added
      a[n]=a[n]%10
      n=n-1
    else: n=-1
  if a[0]==0:     # if no is a permutation of 9's
    a[0]=1
    a.append(0)
  return a

no_add([0,0,9,9])

