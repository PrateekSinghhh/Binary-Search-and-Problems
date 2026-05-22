def sqrt_precision(n, precision=3):
    # Integer part using Binary Search
    s = 0
    e = n
    ans = 0

    while s <= e:
        mid = s + (e - s) // 2

        if mid * mid == n:
            ans = mid
            break

        elif mid * mid < n:
            ans = mid
            s = mid + 1

        else:
            e = mid - 1

    # Decimal precision part
    increment = 0.1
    result = ans

    for _ in range(precision):
        while (result + increment) * (result + increment) <= n:
            result += increment

        increment /= 10

    return result


n = int(input())
p = int(input())   # precision digits

print(sqrt_precision(n, p))