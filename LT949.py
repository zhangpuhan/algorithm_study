class Solution:
    """
    @param n: an integer
    @return: return a string
    """

    def lastFourDigitsOfFn(self, n):
        if n == 0:
            return "0"

        if n == 1:
            return "%04d" % n

        base = [[1, 1], [1, 0]]

        res = self.fast_power(base, n)

        return "%04d" % (res[0][1] % 10000)

    def fast_power(self, base, n):

        if n == 1:
            return base

        temp = self.fast_power(base, n // 2)

        if n % 2 == 0:
            return self.matrix_multi(temp, temp)
        else:
            return self.matrix_multi(self.matrix_multi(temp, temp), base)

    def matrix_multi(self, a, b):
        row, col = len(a), len(a[0])
        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                for k in range(row):
                    res[i][j] += a[i][k] * b[k][j]
                    res[i][j] = res[i][j] % 10000
        return res