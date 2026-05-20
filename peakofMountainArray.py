def peak(arr):
    n=len(arr)
    s=0
    e=n-1
    ans=-1
    
    while s<=e:
        mid=s+(e-s)//2
        if arr[mid]<arr[mid+1]: #ascending part of array
            s=mid+1
        else:
            ans=mid
            
            e=mid-1
    return ans

arr=list(map(int,input().split( )))


peak=peak(arr)

print("Peak index:", peak)
print("Peak element:", arr[peak])