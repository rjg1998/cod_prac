def duplicate(arr):
  index=0
  for i in range(1,len(arr)):
    if arr[i]!=arr[index]:
      index+=1
      arr[index]=arr[i]
  for i in range(index+1,len(arr)):
    arr[i]=0
  return index+1
