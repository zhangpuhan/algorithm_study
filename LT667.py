class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        # write your code here
        l = len(s)

        if l == 0:
            return 0

        dp = [[0] * l for _ in range(l)]

        for i in range(l - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    continue
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][l - 1]