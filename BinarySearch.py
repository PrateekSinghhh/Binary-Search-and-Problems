def binarySearch(arr,n,key):
    s=0
    e=n-1
    
    mid=s+(e-s)//2
    
    while s<=e:
        if arr[mid]==key:
            return mid
        elif key>arr[mid]:
            s=mid+1
        else:
            e=mid-1
        
        mid=s+(e-s)//2
        
    return -1
        
        
even=[2,4,6,7,12,16]

odd=[2,5,6,9,19]

print(binarySearch(even,len(even),7))
print(binarySearch(odd,len(odd),7))
print(binarySearch(odd,len(odd),19))