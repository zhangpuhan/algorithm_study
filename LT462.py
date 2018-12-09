class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        # write your code here

        if not A:
            return 0

        length = len(A)

        start = 0
        end = length - 1

        while start + 1 < end:
            mid = (end + start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            head = start
        elif A[end] == target:
            head = end
        else:
            head = -1

        start = 0
        end = length - 1
        while start + 1 < end:
            mid = (end + start) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            tail = end
        elif A[start] == target:
            tail = start
        else:
            tail = -1

        if head >= 0 and tail >= 0:
            return tail - head + 1
        else:
            return 0