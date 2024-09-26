from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        # i: 0,1,2,3,4
        # j: 0,1,1,2,3
        # 0, 1,

        n = len(nums)
        j = 0

        # iterate through the array
        for i in range(n):
            # if we are at the last element
            if i == n - 1:
                nums[j] = nums[i]
            # if the current element is not equal to the next element
            elif nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j += 1

        return j + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k)
print(nums[:k])
