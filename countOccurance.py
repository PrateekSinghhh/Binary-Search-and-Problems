def lowerBound(arr, target):
    n = len(arr)

    s = 0
    e = n - 1

    ans = n

    while s <= e:

        mid = s + (e - s) // 2

        if arr[mid] >= target:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    return ans


def upperBound(arr, target):
    n = len(arr)

    s = 0
    e = n - 1

    ans = n

    while s <= e:

        mid = s + (e - s) // 2

        if arr[mid] > target:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    return ans


arr = list(map(int, input().split()))
target = int(input())

lb = lowerBound(arr, target)
ub = upperBound(arr, target)

count = ub - lb

print("Count =", count)