class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """

    def spiralOrder(self, matrix):
        # write your code here
        if matrix == []:
            return []

        up = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        left = 0

        direct = 0  # 0 go right, 1 go down, 2 go left, 3 go up

        res = []

        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1

            if direct == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1

            if direct == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1

            if direct == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1

            if left > right or up > down:
                return res

            direct = (direct + 1) % 4