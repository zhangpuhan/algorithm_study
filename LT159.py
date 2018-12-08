class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        length = len(nums)

        start = 0
        end = length - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid

            else:
                end = mid

        return min(nums[start], nums[end])