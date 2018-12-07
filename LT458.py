class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, A, target):
        if not A or target is None:
            return -1

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = (end + start) // 2

            if A[mid] < target:
                start = mid
                continue

            elif A[mid] > target:
                end = mid
                continue

            else:
                start = mid
                continue

        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        else:
            return -1