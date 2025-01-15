arr=[5,2,7,3,10,1]
def DACminmax(arr,i,j):
    if(i==j):
        return arr[i],arr[i]
    elif(i==j-1):
        if(arr[i]>arr[j]):
            return arr[i],arr[j]
        else:
            return arr[j],arr[i]
    else:
        mid=(i+j)//2
    max1,min1=DACminmax(arr,i,mid)
    print(f"max is {max1} and min is {min1}")
    max2,min2=DACminmax(arr,mid+1,j) 
    print(f"max is {max2} and min is {min2}")           
    return max(max1, max2), min(min1, min2)

mini,maxi=DACminmax(arr,0,len(arr)-1)  
print(maxi,mini)
