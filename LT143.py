class quickSort(object):
    def __init__(self, nums, pivot):
        self.A = nums
        self.sort(0, len(self.A) - 1, 0, pivot)

    def sort(self, start, end, pstart, pend):
        if start >= end or pstart >= pend:
            return
        pivot = pstart + (pend - pstart) / 2
        l, r = start, end
        while l <= r:
            while l <= r and self.A[l] <= pivot:
                l += 1
            while l <= r and self.A[r] > pivot:
                r -= 1
            if l <= r:
                self.A[l], self.A[r] = self.A[r], self.A[l]
                l += 1
                r -= 1
        # print pivot,self.A
        self.sort(start, r, pstart, pivot)
        self.sort(l, end, pivot + 1, pend)


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here

        quickSort(colors, k)