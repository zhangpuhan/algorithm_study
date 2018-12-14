class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m * n - 1

        while start + 1 < end:
            mid = (start + end) // 2
            x = mid // n
            y = mid % n

            if matrix[x][y] < target:
                start = mid

            else:
                end = mid

        x = start // n
        y = start % n

        if matrix[x][y] == target:
            return True

        x = end // n
        y = end % n

        if matrix[x][y] == target:
            return True

        return False