def partiation(a,s,e):
    pivot=a[s]
    count=0
    for i in range(s+1,e+1):
        if(a[i]<pivot):
            count=count+1
    pivotindex=s+count
    swap(pivotindex,s)
    i=s
    j=e
    while(i<pivotindex and j<pivotindex):
        while(pivot>a[i]):
            i+=1
        while(pivot<a[j]):
            j-=1    
        if(i<pivotindex and j<pivotindex):
            swap(i,j)
            i+=1
            j-=1
    return pivotindex        
def quicksort(a,s,e):
    if(s>=e):
        return
    p=partiation(a,s,e)
    quicksort(a,s,p-1)
    quicksort(a,p+1,e)

def swap(a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
arr=[93,42,12,53,24,75,23]    
quicksort(arr,0,len(arr)-1)
for i in range(len(arr)):
    print(arr[i])
