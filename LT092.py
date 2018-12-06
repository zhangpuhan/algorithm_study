class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here

        l = len(A)

        f = [[False] * (m + 1) for row in range(l + 1)]

        f[0][0] = True

        for i in range(1, l + 1):
            f[i][0] = True
            for w in range(1, m + 1):
                if w >= A[i - 1]:
                    f[i][w] = f[i - 1][w] or f[i - 1][w - A[i - 1]]
                    continue

                else:
                    f[i][w] = f[i - 1][w]

        for j in range(m, -1, -1):
            if f[l][j] == True:
                return j


        else:
            return 0
