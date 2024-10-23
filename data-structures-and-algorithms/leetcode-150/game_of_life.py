from typing import List


class Solution:

    def get_directions(self, i, j, m, n):
        """
        Generates valid neighboring cell coordinates for a given cell in a 2D grid.

        Args:
            i (int): The row index of the current cell.
            j (int): The column index of the current cell.
            m (int): The total number of rows in the grid.
            n (int): The total number of columns in the grid.

        Yields:
            tuple: A tuple (x, y) representing the coordinates of a neighboring cell
                   that is within the bounds of the grid.
        """
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        for x, y in directions:
            if 0 <= i + x < m and 0 <= j + y < n:
                yield (i + x, j + y)

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Simulates the Game of Life on a given board.

        The Game of Life is a cellular automaton devised by mathematician John Conway.
        The board is a 2D grid where each cell can be either alive (1) or dead (0).
        The next state of each cell is determined by its current state and the number
        of live neighbors it has, according to the following rules:

        1. Any live cell with fewer than two live neighbors dies, as if by under-population.
        2. Any live cell with two or three live neighbors lives on to the next generation.
        3. Any live cell with more than three live neighbors dies, as if by over-population.
        4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        Args:
            board (List[List[int]]): A 2D list representing the initial state of the board.

        Returns:
            None: The board is modified in place to represent the next state.
        """
        m, n = len(board), len(board[0])
        # cache = {}

        for x in range(m):
            for y in range(n):
                live_cnt = 0
                for dx, dy in self.get_directions(x, y, m, n):
                    live_cnt += board[dx][dy] & 1

                # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                # Any live cell with two or three live neighbors lives on to the next generation.
                # Any live cell with more than three live neighbors dies, as if by over-population.
                if board[x][y] == 1 and (live_cnt < 2 or live_cnt > 3):
                    # cache[(x, y)] = 0
                    board[x][y] = -1  # Mark cell as dead

                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                if board[x][y] == 0 and live_cnt == 3:
                    # cache[(x, y)] = 1
                    board[x][y] = 2  # Mark cell as alive

        # Update board
        for x in range(m):
            for y in range(n):
                board[x][y] = 1 if board[x][y] > 0 else 0
                # board[x][y] = cache.get((x, y), board[x][y])

        return board


assert Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]) == [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
]
assert Solution().gameOfLife([[1, 1], [1, 0]]) == [[1, 1], [1, 1]]
assert Solution().gameOfLife([[0, 0], [0, 1]]) == [[0, 0], [0, 0]]
print("Passed all test cases!")
