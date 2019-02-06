class Solution:
    def subsets(self, nums):
        """docstring for subsets"""
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        """docstring for dfs"""
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()


a = Solution()
print(a.subsets([1, 2]))

        
