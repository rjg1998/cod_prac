# -*- coding: utf-8 -*-
"""candies.ipynb


from math import sqrt

def candies(c,n):
  a=int(sqrt(2*c))
  if a*(a+1)/2>c:
    a=a-1
  elif (a+2)*(a+1)/2<c:      ##"a is no of kids requires to distribute candies acc to given mtd"
    a=a+1
  
  l=a//n        ## "l is complete rotations and r is incomplete rotaion no."
  r=a%n

  arr=[0]*n     ## arr is answer array
  for i in range(r):
    arr[i]=(i+1)*(l+1)+int(n*l*(l+1)/2)     # arr[i] for kids in incomplete and complete rotation 
  for i in range(r,n):
    arr[i]=(i+1)*(l)+int(n*(l-1)*l/2)    # arr[i] for only complete rotations
  if c>a*(a+1)/2: 
    arr[(r)%(n)]+=int(c-a*(a+1)/2)        # remaining candies
  return arr
candies(4,10)

