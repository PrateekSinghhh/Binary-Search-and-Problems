"""
    pivot of rotated sorted array
    
    arr = [1,2,3,4,5]
    Our input arr        /     /
    arr=[4,5,1,2,3]     /     /
    outputpivot=5            /   
    """
def pivotRotatedSortedArray(arr):
    n=len(arr)
    s=0
    e=n-1
    ans=-1
    if arr[s] <= arr[e]:
        return -1
    while(s<=e):
        mid=s+(e-s)//2
        if arr[mid]<arr[n-1]:
            e=mid-1
            
        elif arr[mid]>arr[n-1]:
            ans=mid
            s=mid+1
        else:
            e-=1
    return ans
            
    
    
arr=list(map(int,input().split( )))

result = pivotRotatedSortedArray(arr)

if result == -1:
    print("Array is sorted and not rotated")
else:
    print("Pivot index is:", result)
    print("Pivot element is:", arr[result])