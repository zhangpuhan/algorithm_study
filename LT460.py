class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        res = []
        start = 0
        length = len(A)
        end = length - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        right = min(length, end + k)
        left = max(0, start - k)
        search = A[left:right]
        diff = [(abs(target - a), a) for a in search]
        diff = sorted(diff)
        diff = diff[:k]

        for _, x in diff:
            res.append(x)

        return res