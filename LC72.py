class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        f = [[0 for x in range(n+1)] for y in range(m+1)]

        if m*n == 0:
            return m+n

        for j in range(n+1):
            f[0][j] = j

        for i in range(m+1):
            f[i][0] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                left = f[i][j-1] + 1
                up = f[i-1][j] + 1
                up_left = f[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    up_left += 1

                f[i][j] = min(up, left, up_left)

        return f[m][n]
