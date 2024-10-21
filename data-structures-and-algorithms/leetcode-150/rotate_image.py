from typing import List


class Solution:

    def transpose(self, matrix: List[List[int]], n: int) -> None:
        """
        Transposes the given square matrix in place.

        This method swaps the elements at positions (i, j) and (j, i) for all i and j
        such that 0 <= i < n and i <= j < n. This effectively converts rows into columns
        and columns into rows.

        Args:
            matrix (List[List[int]]): The square matrix to be transposed.
            n (int): The dimension of the square matrix.
        """
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, matrix: List[List[int]], n: int) -> None:
        """
        Reverses each row of the given n x n matrix in place.

        Args:
            matrix (List[List[int]]): The n x n matrix to be reversed.
            n (int): The size of the matrix (number of rows/columns).

        Returns:
            None
        """
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the given n x n 2D matrix 90 degrees clockwise in-place.

        Args:
            matrix (List[List[int]]): The n x n 2D matrix to be rotated.

        Returns:
            None: The matrix is modified in-place.
        """

        # Rotate the matrix in-place
        n = len(matrix)

        # Transpose the matrix
        self.transpose(matrix, n)

        # Reverse the matrix
        self.reverse(matrix, n)

        return matrix


assert Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
assert Solution().rotate(
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

assert Solution().rotate([[1]]) == [[1]]

assert Solution().rotate([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

print("All tests passed.")
