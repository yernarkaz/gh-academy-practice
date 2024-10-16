from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize pointers
        start, end = 0, 0

        # Initialize sum and min_len
        s = 0
        min_len = float("inf")

        # Loop through the array
        while end < len(nums):
            # Keep adding to the sum
            s += nums[end]

            # If the sum is greater than or equal to the target
            while s >= target:
                # Update min
                min_len = min(min_len, end - start + 1)

                # Shrink the window
                s -= nums[start]
                start += 1

            # Expand the window
            end += 1

        return min_len if min_len != float("inf") else 0


assert Solution().minSubArrayLen(7, []) == 0
assert Solution().minSubArrayLen(100, [1, 2, 3, 4, 5]) == 0
assert Solution().minSubArrayLen(5, [5]) == 1
assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert Solution().minSubArrayLen(7, [2, 1, 1, 1, 1, 1]) == 6

print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(7, [2, 1, 1, 1, 1, 1]))
