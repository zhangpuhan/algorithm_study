class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        # write your code here
        k = 2
        result = []

        while k * k <= num:
            while num % k == 0:
                result.append(k)
                num //= k

            k += 1

        if num > 1:
            result.append(num)

        return result