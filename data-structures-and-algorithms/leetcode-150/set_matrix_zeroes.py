from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modifies the input matrix such that if an element is 0, its entire row and column are set to 0.

        Args:
            matrix (List[List[int]]): A 2D list of integers representing the matrix.

        Returns:
            None: The function modifies the matrix in place and does not return anything.
        """

        m, n = len(matrix), len(matrix[0])
        is_col = False
        # zero_rows, zero_cols = set(), set()

        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True

            for j in range(1, n):
                if matrix[i][j] == 0:
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    # zero_rows.add(i)
                    # zero_cols.add(j)

        # print(zero_rows, zero_cols)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                # if i in zero_rows or j in zero_cols:
                #     matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if is_col:
            for i in range(m):
                matrix[i][0] = 0

        return matrix


assert Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
]
assert Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0],
]
assert Solution().setZeroes([[1, 1, 1], [1, 1, 1], [1, 1, 0]]) == [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 0],
]
assert Solution().setZeroes([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]
print("All tests passed.")
