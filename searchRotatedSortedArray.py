def findPivot(arr):
    n = len(arr)
    s = 0
    e = n - 1
    ans = -1

    # already sorted
    if arr[s] <= arr[e]:
        return -1

    while s <= e:
        mid = s + (e - s) // 2

        if arr[mid] < arr[n - 1]:
            e = mid - 1
        else:
            ans = mid
            s = mid + 1

    return ans


def binarySearch(arr, s, e, target):

    while s <= e:
        mid = s + (e - s) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            s = mid + 1

        else:
            e = mid - 1

    return -1


def searchRotated(arr, target):

    pivot = findPivot(arr)

    # not rotated
    if pivot == -1:
        return binarySearch(arr, 0, len(arr)-1, target)

    # left side
    if target >= arr[0]:
        return binarySearch(arr, 0, pivot, target)

    # right side
    return binarySearch(arr, pivot + 1, len(arr)-1, target)


arr = list(map(int, input().split()))
target = int(input())

print(searchRotated(arr, target))