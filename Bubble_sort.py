arr=[1,2,3,4,5]
for i in range(len(arr)-1):
    flag=0
    for j in range(len(arr)-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag=1
    if flag==0:
        break
print(arr)
