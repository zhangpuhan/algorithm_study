# O(n)
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1

        return result

# O(nlogn)
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here
        length = len(nums)

        if length == 0:
            return 0

        nums.sort()
        result = 1

        for i in range(1, length):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1

        return result