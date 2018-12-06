class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        merge = []

        while A and B:
            if A[0] < B[0]:
                merge.append(A.pop(0))
            else:
                merge.append(B.pop(0))

        merge += A + B

        return merge