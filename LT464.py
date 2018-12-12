class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # write your code here
        A = self.sorthelper(A)
        print(A)
        return

    def sorthelper(self, A):
        if len(A) <= 1:
            return A

        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        left = self.sorthelper(left)
        right = self.sorthelper(right)

        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))

            else:
                merged.append(right.pop(0))

        return merged + left + right