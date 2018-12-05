class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        house = len(nums)
        dp = [0 for x in range(house)]

        if not house:
            return 0

        if house == 1:
            return nums[0]


        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])


        for i in range(2, house):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])


        return dp[house-1]
