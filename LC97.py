class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 + l2 != l3:
            return False

        dp = [[False for x in range(l2 + 1)] for y in range(l1 + 1)]

        dp[0][0] = True

        for i in range(1, l1 + 1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True

        for j in range(1, l2 + 1):
            if s2[:j] == s3[:j]:
                dp[0][j] = True

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                dp[i][j] = (dp[i-1][j] and (s3[i+j-1] == s1[i-1])) or \
                    (dp[i][j-1] and (s3[i+j-1] == s2[j-1]))



        return dp[l1][l2]
