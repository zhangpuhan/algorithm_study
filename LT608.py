class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        if not nums:
            return []

        left, right = 0, len(nums) - 1
        while left < right:
            res = target - nums[left]
            if res == nums[right]:
                break
            elif res < nums[right]:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]