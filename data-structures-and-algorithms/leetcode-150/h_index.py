from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 3,0,6,1,5 = 3
        # 6,5,3,1,0
        # 1,2,3,4,5,6,7,8

        # 1,3,1 = 1 => 1,1,3
        # 1,0,1,2,3,1,2,3,2 = 2
        # 0,1,1,1,2,2,2,3,3
        # 1,2,3,4,5,6,7,8,9

        citations.sort(reverse=True)
        n = len(citations)
        h_index = 0

        for i in range(n):
            if citations[i] > i:
                h_index = i + 1

        return h_index


print(Solution().hIndex([3, 0, 6, 1, 5]))  # 3
