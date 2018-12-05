class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1

        l, r = 0, x

        while l <= r:
            mid = (l+r)//2

            if mid*mid <= x < (mid+1)*(mid+1):
                return mid

            elif mid*mid > x:
                r = mid

            else:
                l = mid
