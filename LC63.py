class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for x in range(n)] for y in range(m)]

        if not obstacleGrid[0][0]:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i and j:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                        continue
                    if (not j) and i:
                        dp[i][j] = dp[i-1][j]
                        continue
                    if (not i) and j:
                        dp[i][j] = dp[i][j-1]
                        continue



        return dp[m-1][n-1]
