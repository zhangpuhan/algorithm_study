class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        # a ^ n % b
        if n == 0:
            return 1 % b

        ans = 1
        power = a
        while n > 0:
            if n % 2 == 1:
                ans = ans * power % b

            power = (power * power) % b
            n = n // 2

        return ans