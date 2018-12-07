class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        ls = len(source)
        lt = len(target)

        if lt > ls:
            return -1

        if lt == ls:
            if source == target:
                return 0
            else:
                return -1

        for i in range(ls - lt + 1):
            if target == source[i:lt + i]:
                return i

        return -1