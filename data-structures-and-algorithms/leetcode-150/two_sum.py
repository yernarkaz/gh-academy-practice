from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach 1: brute force all pairs to find the right pair equals to target O(n^2)
        # approach 2: use hashmap to store complement O(n)

        complement = dict()

        # 3,2,4 t = 6
        # {3:0, 4:1, 2:2}
        for i, num in enumerate(nums):
            complement[target - num] = i

        for i, num in enumerate(nums):
            if num in complement and complement[num] != i:
                return [complement[num], i]

        return [-1, -1]


Solution().twoSum([3, 2, 4], 6)  # [1, 2]
Solution().twoSum([2, 7, 11, 15], 9)  # [0, 1]
Solution().twoSum([3, 3], 6)  # [0, 1]
