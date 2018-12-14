class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        res = 1
        sum = 1
        while sum < n:
            res += 1
            sum += res
        return res