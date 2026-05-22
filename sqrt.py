def nearest_sqrt(n):
    s = 0
    e = n
    ans = 0

    while s <= e:
        mid = s + (e - s) // 2

        if mid * mid == n:
            return mid

        elif mid * mid < n:
            ans = mid
            s = mid + 1

        else:
            e = mid - 1

    return ans


n = int(input())
print(nearest_sqrt(n))