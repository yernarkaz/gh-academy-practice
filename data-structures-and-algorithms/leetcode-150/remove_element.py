from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3,2,2,3] val = 3
        # [3=2,2,_,_]

        # init two pointers
        # i is the index of the current element being processed

        n = len(nums)
        j = 0
        for i in range(n):
            # if the current element is not equal to val
            if nums[i] != val:
                # j is the index of the next element to be replaced
                nums[j] = nums[i]
                j += 1

        return j


nums = [3, 2, 2, 3]
k = Solution().removeElement(nums, 3)
print(nums[:k])


nums = [3, 2, 2, 3, 3, 3]
k = Solution().removeElement(nums, 2)
print(nums[:k])
