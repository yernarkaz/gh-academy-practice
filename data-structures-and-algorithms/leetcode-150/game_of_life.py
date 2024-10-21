from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        pass


assert Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]) == [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
]
assert Solution().gameOfLife([[1, 1], [1, 0]]) == [[1, 1], [1, 1]]
assert Solution().gameOfLife([[0, 0], [0, 1]]) == [[0, 0], [0, 0]]
