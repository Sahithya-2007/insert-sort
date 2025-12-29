def insertsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        for j in range(i-1):
            while j>=0 and arr[j]>key:
                  arr[j+1]=arr[j]
                  j-=i-1
                  arr[j+1]=key
                  return arr
arr=[8,3,5,2]
print(insertsort(arr))