from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given a 2D matrix, return all elements of the matrix in spiral order.

        Args:
            matrix (List[List[int]]): A 2D list of integers representing the matrix.

        Returns:
            List[int]: A list of integers representing the elements of the matrix in spiral order.

        Example:
            >>> matrix = [
            ...     [1, 2, 3],
            ...     [4, 5, 6],
            ...     [7, 8, 9]
            ... ]
            >>> spiralOrder(matrix)
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        """

        # Initialize variables
        m, n = len(matrix), len(matrix[0])
        res = []

        # Initialize boundaries
        left, right, top, bottom = 0, 0, 0, 0
        # Initialize pointers
        i, j, k = 0, 0, 0

        # Total number of elements in the matrix
        l = m * n  # noqa: E741

        # Traverse the matrix in spiral order
        while k < l:

            # Traverse right
            while j < n - right and k < l:
                res.append(matrix[i][j])
                j += 1
                k += 1

            i += 1
            j -= 1

            # Traverse down
            while i < m - bottom and k < l:
                res.append(matrix[i][j])
                i += 1
                k += 1

            j -= 1
            i -= 1

            # Traverse left
            while j > left - 1 and k < l:
                res.append(matrix[i][j])
                j -= 1
                k += 1

            i -= 1
            j += 1

            # Traverse up
            while i > top and k < l:
                res.append(matrix[i][j])
                i -= 1
                k += 1

            j += 1
            i += 1

            right += 1
            bottom += 1
            left += 1
            top += 1

        return res


assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    1,
    2,
    3,
    6,
    9,
    8,
    7,
    4,
    5,
]
assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
    1,
    2,
    3,
    4,
    8,
    12,
    11,
    10,
    9,
    5,
    6,
    7,
]
assert Solution().spiralOrder(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
print("Passed all test cases!")
