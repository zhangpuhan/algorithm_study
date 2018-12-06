class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: how many problem can you accept
    """

    def canAccept(self, n, k):
        # Write your code here

        upperlimit = n // k

        left = 1
        right = upperlimit

        while right > left:
            mid = (left + right) // 2

            if (1 + mid) * mid / 2 <= upperlimit and \
                    (1 + mid + 1) * (mid + 1) / 2 > upperlimit:
                break

            if (1 + mid) * mid / 2 > upperlimit:
                right = mid

            if (1 + mid) * mid / 2 < upperlimit:
                left = mid

        return mid
