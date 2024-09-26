from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        left = n - 1

        # iterate from right to left
        for i in range(n - 2, -1, -1):
            # if we can reach the leftmost index from this index
            if i + nums[i] >= left:
                # update the leftmost index
                left = i
        # if the leftmost index is 0, we can reach the end
        return left == 0


print(Solution().jump([2, 3, 1, 1, 4]))  # True
print(Solution().jump([1, 2, 0, 1, 4]))  # True
print(Solution().jump([1, 1, 0, 1, 4]))  # False
