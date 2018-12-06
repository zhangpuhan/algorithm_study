class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """

    def myPow(self, x, n):
        # write your code here

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 1:
            return x * self.myPow(x, n - 1)

        else:
            return self.myPow(x * x, n / 2)