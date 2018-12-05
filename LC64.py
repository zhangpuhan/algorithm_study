class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for x in range(n)] for y in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if (not i) and j:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                if (not j) and i:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                if i and j:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]
