from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        right, end = 0, 0
        min_jumps = 0

        for i in range(n - 1):
            # update the rightmost index
            right = max(right, i + nums[i])

            # if we reach the end of the current jump
            if i == end:
                min_jumps += 1
                end = right

        return min_jumps


print(Solution().jump([2, 3, 1, 1, 4]))  # 2
print(Solution().jump([1, 2, 0, 1, 4]))  # 3
