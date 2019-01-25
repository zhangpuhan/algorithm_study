def divide(dividend, divisor):
    INT_MAX = 2147483647
    if divisor == 0:
        return INT_MAX
    neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
    a, b = abs(dividend), abs(divisor)
    ans, shift = 0, 31
    while shift >= 0:
        print(a, b)
        print(b << shift)
        if a >= b << shift:
            a -= b << shift
            print(ans)
            ans += 1 << shift
        shift -= 1
    if neg:
        ans = - ans
    if ans > INT_MAX:
        return INT_MAX
    return ans

print(divide(100, 9))