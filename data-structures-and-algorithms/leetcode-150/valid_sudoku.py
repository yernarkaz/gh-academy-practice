from typing import List


class Solution:
    def isRowValid(self, board: List[List[str]]) -> bool:
        """
        Checks if each row in the given Sudoku board is valid.

        A row is considered valid if it contains no duplicate numbers
        (ignoring empty cells represented by '.').

        Args:
            board (List[List[str]]): A 2D list representing the Sudoku board.

        Returns:
            bool: True if all rows are valid, False otherwise.
        """
        for row in board:
            row_dict = {}
            for cell in row:
                if cell != ".":
                    if cell in row_dict:
                        return False
                    row_dict[cell] = True
        return True

    def isColumnValid(self, board: List[List[str]]) -> bool:
        """
        Checks if all columns in the given Sudoku board are valid.

        A column is valid if it contains the digits 1-9 without repetition.

        Args:
            board (List[List[str]]): A 2D list representing the Sudoku board,
                                     where each element is a string (either a digit '1'-'9' or '.').

        Returns:
            bool: True if all columns are valid, False otherwise.
        """
        n = len(board[0])
        for j in range(n):
            column_dict = {}
            for i in range(n):
                cell = board[i][j]
                if cell != ".":
                    if cell in column_dict:
                        return False
                    column_dict[cell] = True
        return True

    def isGridValid(self, grid: List[List[str]]) -> bool:
        """
        Checks if a 3x3 Sudoku grid is valid.

        A valid Sudoku grid means that no number appears more than once in the grid.

        Args:
            grid (List[List[str]]): A 2D list representing the Sudoku grid, where each element is a string.
                                    Empty cells are represented by the character '.'.

        Returns:
            bool: True if the grid is valid, False otherwise.
        """
        values = [val for row in grid for val in row if val != "."]
        return len(values) == len(set(values))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_valid = self.isRowValid(board)
        column_valid = self.isColumnValid(board)

        grid_valid_list = []
        n = len(board[0])
        step = 3

        for i in range(0, n, step):
            for j in range(0, n, step):
                grid = []
                for k in range(i, i + step):
                    grid.append(board[k][j : j + step])
                grid_valid_list.append(self.isGridValid(grid))

        grid_valid = all(grid_valid_list)

        return row_valid and column_valid and grid_valid


assert (
    Solution().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    is True
)

assert (
    Solution().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    is not True
)

print("All tests passed.")
