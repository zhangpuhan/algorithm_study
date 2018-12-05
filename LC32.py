class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ns = len(s)
        dp = [0 for x in range(ns)]
        umax = 0

        for i in range(1, ns):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == "(":
                    if dp[i-1] > 0:
                        dp[i] = dp[i-1] + dp[i- dp[i-1] - 2] + 2
                    else: dp[i] = 0

            umax = max(dp[i], umax)


        return umax
